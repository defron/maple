import os
import uuid
from collections.abc import AsyncGenerator, Sequence
from datetime import datetime
from typing import Annotated, Any, cast

import msgspec
from advanced_alchemy import AsyncSessionConfig, ConflictError
from litestar import Litestar, delete, get, post, put
from litestar.config.compression import CompressionConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from litestar.contrib.sqlalchemy.plugins.init.config.common import SESSION_SCOPE_KEY, SESSION_TERMINUS_ASGI_EVENTS
from litestar.di import Provide
from litestar.enums import RequestEncodingType
from litestar.exceptions import ClientException, HTTPException, MethodNotAllowedException, NotFoundException
from litestar.params import Body
from litestar.status_codes import HTTP_200_OK, HTTP_204_NO_CONTENT, HTTP_409_CONFLICT
from litestar.utils import delete_litestar_scope_state, get_litestar_scope_state
from sqlalchemy import NullPool, func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import joinedload, noload

from app.config import MAPLE_CONFIG
from app.dto.entities import (
    Account,
    AccountType,
    Category,
    Institution,
    TimeSpan,
    Transaction,
    TransactionSource,
    TransactionTag,
)
from app.dto.models import (
    AccountDTO,
    AccountRequestModel,
    AccountResponseModel,
    CategoryRequestModel,
    CategoryResponseModel,
    CsvTransactionsRequest,
    InstitutionRequestModel,
    InstitutionResponseModel,
    ManualTransactionRequest,
    TagRequestModel,
    TagResponseModel,
    TransactionDTO,
    UpdateAccountRequestModel,
)
from app.dto.repos import (
    AccountRepository,
    CategoryRepository,
    InstitutionRepository,
    TagRepository,
    TransactionRepository,
)
from app.helpers.transaction_hash_helper import transaction_hash


async def provide_institution_repo(db_session: AsyncSession) -> InstitutionRepository:
    """This provides the default Institutions repository."""
    return InstitutionRepository(session=db_session)


async def provide_tag_repo(db_session: AsyncSession) -> TagRepository:
    """This provides the default Tag repository."""
    return TagRepository(session=db_session)


async def provide_category_repo(db_session: AsyncSession) -> CategoryRepository:
    """This provides the default Category repository."""
    return CategoryRepository(session=db_session)


async def provide_account_repo(db_session: AsyncSession) -> AccountRepository:
    """This provides the default Account repository."""
    return AccountRepository(session=db_session)


async def provide_transaction_repo(db_session: AsyncSession) -> TransactionRepository:
    """This provides the default Account repository."""
    return TransactionRepository(session=db_session)


async def provide_transaction(db_session: AsyncSession) -> AsyncGenerator[AsyncSession, None]:
    try:
        async with db_session.begin():
            yield db_session
    except IntegrityError as e:
        raise ClientException(
            status_code=HTTP_409_CONFLICT,
            detail=str(e),
        ) from e


async def select_account_types(session: AsyncSession, id: int | None = None) -> Sequence[AccountType] | None:
    query = select(AccountType)
    try:
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as e:
        print(e)
        return None


async def get_account_type(session: AsyncSession, id: int) -> AccountType:
    query = select(AccountType).where(AccountType.id == id)
    result = await session.execute(query)
    return result.scalar_one()


# TODO: are these timespans translating correctly?
async def select_timespans(session: AsyncSession) -> Sequence[TimeSpan] | None:
    query = select(TimeSpan)
    try:
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as e:
        print(e)
        return None


async def select_categories(session: AsyncSession) -> Sequence[Category] | None:
    query = (
        select(Category)
        .options(joinedload(Category.subcategories))
        .where(Category.parent_category_id.is_(None))
        .order_by(Category.id)
    )
    try:
        result = await session.execute(query)
        return result.unique().scalars().all()
    except Exception as e:
        print(e)
        return None


async def select_sources(session: AsyncSession) -> Sequence[TransactionSource] | None:
    query = select(TransactionSource)
    try:
        result = await session.execute(query)
        return result.unique().scalars().all()
    except Exception as e:
        print(e)
        return None


async def select_institutions(session: AsyncSession) -> Sequence[Institution] | None:
    query = select(Institution)
    try:
        result = await session.execute(query)
        return result.unique().scalars().all()
    except Exception as e:
        print(e)
        return None


async def select_tags(session: AsyncSession) -> Sequence[TransactionTag] | None:
    query = select(TransactionTag)
    try:
        result = await session.execute(query)
        return result.unique().scalars().all()
    except Exception as e:
        print(e)
        return None


async def select_accounts(session: AsyncSession, include_inactive: bool = False) -> Sequence[Account] | None:
    query = (
        select(Account)
        .options(
            joinedload(Account.account_type),
            joinedload(Account.transaction_rules),
            noload(Account.institution),
            noload(Account.bills),
        )
        .order_by(Account.id)
    )
    if not include_inactive:
        query.where(Account.is_active)
    try:
        result = await session.execute(query)
        return result.unique().scalars().all()
    except Exception as e:
        print(e)
        return None


async def select_transactions(session: AsyncSession, account_id: int | None = None) -> Sequence[Transaction] | None:
    query = (
        select(Transaction)
        .options(
            joinedload(Transaction.category), joinedload(Transaction.subtransactions), joinedload(Transaction.tags)
        )
        .order_by(Transaction.txn_date.desc(), Transaction.id)
    )
    if account_id is not None:
        query.where(Transaction.account_id == account_id)
    try:
        result = await session.execute(query)
        return result.unique().scalars().all()
    except Exception as e:
        print(e)
        return None


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/api/account-types", status_code=HTTP_200_OK)
async def get_account_types(transaction: AsyncSession) -> Sequence[AccountType]:
    res = await select_account_types(transaction)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@get("/api/categories", status_code=HTTP_200_OK)
async def get_categories(transaction: AsyncSession) -> Sequence[Category]:
    res = await select_categories(transaction)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@post("/api/category", dependencies={"category_repo": Provide(provide_category_repo)})
async def create_category(category_repo: CategoryRepository, data: CategoryRequestModel) -> CategoryResponseModel:
    if data.parent_category_id is not None:
        parent = await category_repo.get(data.parent_category_id)
        if parent.parent_category_id is not None:
            raise MethodNotAllowedException(detail="Parent category is not a top-level category")
    obj = await category_repo.add(
        Category(**data.model_dump(exclude_unset=True, exclude_none=True)),
    )
    await category_repo.session.commit()
    return CategoryResponseModel.model_validate(obj)


@put("/api/category/{id:int}", dependencies={"category_repo": Provide(provide_category_repo)})
async def update_category(
    category_repo: CategoryRepository, data: CategoryRequestModel, id: int
) -> CategoryResponseModel:
    timestamp = datetime.now()
    obj = await category_repo.update(
        Category(id=id, updated_dt=timestamp, **data.model_dump(exclude_unset=True, exclude_none=True)),
    )
    await category_repo.session.commit()
    return CategoryResponseModel.model_validate(obj)


@delete(
    "/api/category/{id:int}",
    status_code=HTTP_204_NO_CONTENT,
    dependencies={"category_repo": Provide(provide_category_repo)},
)
async def delete_category(category_repo: CategoryRepository, id: int) -> None:
    pending_delete = await category_repo.get(id)
    if pending_delete.is_protected:
        raise MethodNotAllowedException(detail="Default categories cannot be deleted")
    obj = await category_repo.delete(id)
    if obj.id == id:
        await category_repo.session.commit()
        return None
    raise NotFoundException(detail="No data found")


@get("/api/timespans", status_code=HTTP_200_OK)
async def get_timespans(transaction: AsyncSession) -> Sequence[TimeSpan]:
    res = await select_timespans(transaction)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@get("/api/available-sources", status_code=HTTP_200_OK)
async def get_available_sources(transaction: AsyncSession) -> Sequence[TransactionSource]:
    res = await select_sources(transaction)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@get("/api/institutions", status_code=HTTP_200_OK)
async def get_institutions(transaction: AsyncSession) -> Sequence[Institution]:
    res = await select_institutions(transaction)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@post("/api/institution", dependencies={"institution_repo": Provide(provide_institution_repo)})
async def create_institution(
    institution_repo: InstitutionRepository, data: InstitutionRequestModel
) -> InstitutionResponseModel:
    obj = await institution_repo.add(
        Institution(**data.model_dump(exclude_unset=True, exclude_none=True)),
    )
    await institution_repo.session.commit()
    return InstitutionResponseModel.model_validate(obj)


@put("/api/institution/{id:int}", dependencies={"institution_repo": Provide(provide_institution_repo)})
async def update_institution(
    institution_repo: InstitutionRepository, data: InstitutionRequestModel, id: int
) -> InstitutionResponseModel:
    timestamp = datetime.now()
    obj = await institution_repo.update(
        Institution(id=id, updated_dt=timestamp, **data.model_dump(exclude_unset=True, exclude_none=True)),
    )
    await institution_repo.session.commit()
    return InstitutionResponseModel.model_validate(obj)


@delete(
    "/api/institution/{id:int}",
    status_code=HTTP_204_NO_CONTENT,
    dependencies={"institution_repo": Provide(provide_institution_repo)},
)
async def remove_institution(institution_repo: InstitutionRepository, id: int) -> None:
    associated_accounts_count = (
        await institution_repo.session.execute(select(func.count(Account.id)).where(Account.institution_id == id))
    ).scalar()
    if associated_accounts_count is not None and associated_accounts_count > 0:
        raise MethodNotAllowedException(detail="Cannot delete an institution with accounts associated with it")
    obj = await institution_repo.delete(id)
    if obj.id == id:
        await institution_repo.session.commit()
        return None
    raise NotFoundException(detail="No data found")


@get("/api/tags", status_code=HTTP_200_OK)
async def get_tags(transaction: AsyncSession) -> Sequence[TransactionTag]:
    res = await select_tags(transaction)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@post("/api/tags", dependencies={"tag_repo": Provide(provide_tag_repo)})
async def create_tags(tag_repo: TagRepository, data: list[TagRequestModel]) -> list[TagResponseModel]:
    try:
        objs = await tag_repo.add_many(
            [TransactionTag(**raw_obj.model_dump(exclude_unset=True, exclude_none=True)) for raw_obj in data]
        )
        await tag_repo.session.commit()
        return [TagResponseModel.model_validate(obj) for obj in objs]
    except ConflictError as e:
        print(e)
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="At least one tag already exists")


@delete("/api/tag/{id:int}", status_code=HTTP_204_NO_CONTENT, dependencies={"tag_repo": Provide(provide_tag_repo)})
async def delete_tag(tag_repo: TagRepository, id: int) -> None:
    obj = await tag_repo.delete(id)
    if obj.id == id:
        await tag_repo.session.commit()
        return None
    raise NotFoundException(detail="No data found")


@get("/api/accounts", return_dto=AccountDTO, status_code=HTTP_200_OK)
async def get_accounts(transaction: AsyncSession) -> Sequence[Account]:
    res = await select_accounts(transaction, False)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@get("/api/accounts/all", return_dto=AccountDTO, status_code=HTTP_200_OK)
async def get_all_accounts(transaction: AsyncSession) -> Sequence[Account]:
    res = await select_accounts(transaction, True)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@post("/api/account", dependencies={"account_repo": Provide(provide_account_repo)})
async def create_account(account_repo: AccountRepository, data: AccountRequestModel) -> AccountResponseModel:
    obj = await account_repo.add(Account(is_active=True, **data.model_dump(exclude_unset=True, exclude_none=True)))
    await account_repo.session.refresh(obj, ["account_type"])
    await account_repo.session.commit()
    return AccountResponseModel.model_validate(obj)


@delete(
    "/api/account/{id:int}",
    status_code=HTTP_204_NO_CONTENT,
    dependencies={"account_repo": Provide(provide_account_repo)},
)
async def delete_account(account_repo: AccountRepository, id: int) -> None:
    obj = await account_repo.delete(id)
    if obj.id == id:
        await account_repo.session.commit()
        return None
    raise NotFoundException(detail="No data found")


@put("/api/account/{id:int}", dependencies={"account_repo": Provide(provide_account_repo)})
async def update_account(
    account_repo: AccountRepository, data: UpdateAccountRequestModel, id: int
) -> AccountResponseModel:
    timestamp = datetime.now()
    obj = await account_repo.update(
        Account(id=id, updated_dt=timestamp, **data.model_dump(exclude_unset=True, exclude_none=True)),
    )
    await account_repo.session.refresh(obj, ["account_type"])
    await account_repo.session.commit()
    return AccountResponseModel.model_validate(obj)


@get("/api/transactions/{account_id:int}/all", return_dto=TransactionDTO, status_code=HTTP_200_OK)
async def get_all_transactions_for_account(transaction: AsyncSession, account_id: int) -> Sequence[Transaction]:
    # TODO: need to change this and add date filter
    res = await select_transactions(transaction, account_id)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@post(
    "/api/transaction/manual",
    return_dto=TransactionDTO,
    dependencies={"transaction_repo": Provide(provide_transaction_repo)},
)
async def create_manual_transaction(
    transaction_repo: TransactionRepository, data: ManualTransactionRequest
) -> Transaction:
    # TODO: I don't like this being right here
    source_id = uuid.UUID("74f21da5-5bf9-485d-a934-7a9509aa18a8")
    hash = transaction_hash(data.txn_date, data.amount, data.txn_type, data.label or "")
    matches = await transaction_repo.count(
        statement=select(Transaction)
        .where(Transaction.txn_hash == hash)
        .where(Transaction.txn_date == data.txn_date)
        .where(Transaction.account_id == data.account_id)
    )
    matches += 1
    obj = await transaction_repo.add(
        Transaction(
            soft_delete=False,
            is_pending=False,
            txn_source_id=source_id,
            txn_hash=hash,
            daycount=matches,
            source_metadata={},
            **data.model_dump(exclude_unset=True, exclude_none=True),
        )
    )
    await transaction_repo.session.refresh(obj, ["category", "subtransactions", "tags"])
    await transaction_repo.session.commit()
    return obj


@put(
    "/api/transaction/{id:int}",
    return_dto=TransactionDTO,
    dependencies={"transaction_repo": Provide(provide_transaction_repo)},
)
async def update_transaction(
    transaction_repo: TransactionRepository, data: ManualTransactionRequest, id: int
) -> Transaction:
    timestamp = datetime.now()
    obj = await transaction_repo.update(
        Transaction(id=id, updated_dt=timestamp, **data.model_dump(exclude_unset=True, exclude_none=True)),
    )
    await transaction_repo.session.refresh(obj, ["category", "subtransactions", "tags"])
    await transaction_repo.session.commit()
    return obj


@post(
    "/api/transactions/csv",
    return_dto=TransactionDTO,
    dependencies={"transaction_repo": Provide(provide_transaction_repo)},
)
async def add_bulk_transactions_csv(
    transaction_repo: TransactionRepository,
    data: Annotated[CsvTransactionsRequest, Body(media_type=RequestEncodingType.MULTI_PART)],
) -> None:
    # TODO: I don't like this being right here
    source_id = uuid.UUID("993982ef-1dc4-4982-b9a0-4f7185d60250")
    print(data)
    print(source_id)
    _category_mapping = msgspec.json.decode(buf=(data.category_mapping or "{'*': 1}"), type=dict[str, int])
    # load relevant account type detail before the connection is closed
    _acct_type_details = await transaction_repo.session.execute(select(Category))
    # hash = transaction_hash(data.txn_date, data.amount, data.txn_type, data.label or "")
    # matches = await transaction_repo.count(
    #     statement=select(Transaction)
    #     .where(Transaction.txn_hash == hash)
    #     .where(Transaction.txn_date == data.txn_date)
    #     .where(Transaction.account_id == data.account_id)
    # )
    # matches += 1
    # obj = await transaction_repo.add(
    #     Transaction(
    #         soft_delete=False,
    #         is_pending=False,
    #         txn_source_id=source_id,
    #         txn_hash=hash,
    #         daycount=matches,
    #         source_metadata={},
    #         **data.model_dump(exclude_unset=True, exclude_none=True),
    #     )
    # )
    # await transaction_repo.session.refresh(obj, ["category", "subtransactions", "tags"])
    # await transaction_repo.session.commit()
    return None


config = MAPLE_CONFIG


__engine = create_async_engine(
    f"postgresql+asyncpg://{config.db_user}:{os.environ[config.db_password_key]}@{config.db_host}:{config.db_port}/{config.db_name}",
    connect_args={"server_settings": dict(search_path=config.db_search_schema)},
    echo=config.db_echo,
    echo_pool=config.db_echo_pool,
    # json_serializer=msgspec.json.Encoder(enc_hook=_default),
    max_overflow=config.db_max_oveflow,
    pool_size=config.db_pool_size,
    pool_timeout=config.db_pool_timeout,
    poolclass=NullPool if config.db_pool_disable else None,
)

async_session_factory = async_sessionmaker(__engine, expire_on_commit=False, class_=AsyncSession)


async def before_send_handler(message: Any, scope: Any) -> None:
    """Custom `before_send_handler` for SQLAlchemy plugin that inspects the
    status of response and commits, or rolls back the database.

    Args:
        message: ASGI message
        _:
        scope: ASGI scope
    """
    session = cast("AsyncSession | None", get_litestar_scope_state(scope, SESSION_SCOPE_KEY))
    try:
        if session is not None and message["type"] == "http.response.start":
            if 200 <= message["status"] < 300:
                await session.commit()
            else:
                await session.rollback()
    finally:
        if session is not None and message["type"] in SESSION_TERMINUS_ASGI_EVENTS:
            await session.close()
            delete_litestar_scope_state(scope, SESSION_SCOPE_KEY)


session_config = AsyncSessionConfig(expire_on_commit=False)

_db_config = SQLAlchemyAsyncConfig(
    session_dependency_key="db_session",
    engine_instance=__engine,
    session_maker=async_session_factory,
    before_send_handler=before_send_handler,
    session_config=session_config,
)


__app = Litestar(
    [
        index,
        get_account_types,
        get_categories,
        create_category,
        update_category,
        delete_category,
        get_timespans,
        get_available_sources,
        get_institutions,
        create_institution,
        remove_institution,
        update_institution,
        get_tags,
        create_tags,
        delete_tag,
        get_accounts,
        get_all_accounts,
        create_account,
        delete_account,
        update_account,
        create_manual_transaction,
        get_all_transactions_for_account,
        add_bulk_transactions_csv,
    ],
    dependencies={"transaction": provide_transaction},
    plugins=[SQLAlchemyPlugin(_db_config)],
    compression_config=CompressionConfig(
        backend="brotli", brotli_quality=5, brotli_gzip_fallback=True, gzip_compress_level=6
    ),
)


def Maple() -> Litestar:
    return __app
