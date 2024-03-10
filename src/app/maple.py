import os
from collections.abc import AsyncGenerator, Sequence
from typing import Any, cast

from advanced_alchemy import ConflictError
from litestar import Litestar, get, post
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from litestar.contrib.sqlalchemy.plugins.init.config.common import SESSION_SCOPE_KEY, SESSION_TERMINUS_ASGI_EVENTS
from litestar.di import Provide
from litestar.exceptions import ClientException, HTTPException, NotFoundException
from litestar.status_codes import HTTP_200_OK, HTTP_409_CONFLICT
from litestar.utils import delete_litestar_scope_state, get_litestar_scope_state
from sqlalchemy import NullPool, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import joinedload

from app.config import MapleConfig
from app.dto.entities import (
    AccountType,
    Category,
    Institution,
    InstitutionRepository,
    InstitutionRequestModel,
    InstitutionResponseModel,
    TagRepository,
    TagRequestModel,
    TagResponseModel,
    TimeSpan,
    TransactionSource,
    TransactionTag,
)


async def provide_institution_repo(db_session: AsyncSession) -> InstitutionRepository:
    """This provides the default Institutions repository."""
    return InstitutionRepository(session=db_session)


async def provide_tag_repo(db_session: AsyncSession) -> TagRepository:
    """This provides the default Institutions repository."""
    return TagRepository(session=db_session)


async def provide_transaction(db_session: AsyncSession) -> AsyncGenerator[AsyncSession, None]:
    try:
        async with db_session.begin():
            yield db_session
    except IntegrityError as e:
        raise ClientException(
            status_code=HTTP_409_CONFLICT,
            detail=str(e),
        ) from e


async def select_account_types(session: AsyncSession) -> Sequence[AccountType] | None:
    query = select(AccountType)
    try:
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as e:
        print(e)
        return None


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
    query = select(Category).options(joinedload(Category.subcategories)).where(Category.parent_category_id.is_(None))
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


@post("/api/institutions", sync_to_thread=False, dependencies={"institution_repo": Provide(provide_institution_repo)})
async def create_institution(
    institution_repo: InstitutionRepository, data: InstitutionRequestModel
) -> InstitutionResponseModel:
    obj = await institution_repo.add(
        Institution(**data.model_dump(exclude_unset=True, exclude_none=True)),
    )
    await institution_repo.session.commit()
    return InstitutionResponseModel.model_validate(obj)


@get("/api/tags", status_code=HTTP_200_OK)
async def get_tags(transaction: AsyncSession) -> Sequence[TransactionTag]:
    res = await select_tags(transaction)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


@post("/api/tags", sync_to_thread=False, dependencies={"tag_repo": Provide(provide_tag_repo)})
async def create_tag(tag_repo: TagRepository, data: list[TagRequestModel]) -> list[TagResponseModel]:
    try:
        objs = await tag_repo.add_many(
            [TransactionTag(**raw_obj.model_dump(exclude_unset=True, exclude_none=True)) for raw_obj in data]
        )
        await tag_repo.session.commit()
        return [TagResponseModel.model_validate(obj) for obj in objs]
    except ConflictError as e:
        print(e)
        raise HTTPException(status_code=HTTP_409_CONFLICT, detail="At least one tag already exists")


config = MapleConfig()

# TODO: put these in a config
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


_db_config = SQLAlchemyAsyncConfig(
    session_dependency_key="db_session",
    engine_instance=__engine,
    session_maker=async_session_factory,
    before_send_handler=before_send_handler,
)

__app = Litestar(
    [
        index,
        get_account_types,
        get_categories,
        get_timespans,
        get_available_sources,
        get_institutions,
        create_institution,
        get_tags,
        create_tag,
    ],
    dependencies={"transaction": provide_transaction},
    plugins=[SQLAlchemyPlugin(_db_config)],
)


def Maple() -> Litestar:
    return __app
