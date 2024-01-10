from typing import Any, cast
import datetime
from collections.abc import AsyncGenerator, Sequence
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from litestar import Litestar, get
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from litestar.exceptions import ClientException, NotFoundException
from litestar.status_codes import HTTP_409_CONFLICT, HTTP_200_OK
from litestar.utils import delete_litestar_scope_state, get_litestar_scope_state
from litestar.contrib.sqlalchemy.plugins.init.config.common import (
    SESSION_SCOPE_KEY,
    SESSION_TERMINUS_ASGI_EVENTS,
)
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import msgspec
from sqlalchemy import event


class Base(DeclarativeBase):
    ...


class AccountType(Base):
    __tablename__ = "account_type"
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    is_asset: Mapped[bool]
    created_dt: Mapped[datetime.datetime]
    updated_dt: Mapped[datetime.datetime]


async def provide_transaction(
    db_session: AsyncSession,
) -> AsyncGenerator[AsyncSession, None]:
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


@get("/")
async def index() -> str:
    return "Hello, world!"


@get("/api/account-types", status_code=HTTP_200_OK)
async def get_account_types(transaction: AsyncSession) -> Sequence[AccountType]:
    res = await select_account_types(transaction)
    if res is None:
        raise NotFoundException(detail="No data found")
    return res


def _default(val: Any) -> str:
    if isinstance(val, UUID):
        return str(val)
    raise TypeError()


_settings = dict(search_path="maple")

# TODO: put these in a config
__engine = create_async_engine(
    "postgresql+asyncpg://devuser:devpass@127.0.0.1:54320/maple",
    connect_args={"server_settings": _settings},
    echo=False,
    json_serializer=msgspec.json.Encoder(enc_hook=_default),
    max_overflow=10,
    pool_size=5,
    pool_timeout=30,
    poolclass=None,
)

async_session_factory = async_sessionmaker(
    __engine, expire_on_commit=False, class_=AsyncSession
)


@event.listens_for(__engine.sync_engine, "connect")
def sqla_on_connect(dbapi_connection: Any, _: Any) -> Any:
    """Using orjson for serialization of the json column values means that the
    output is binary, not `str` like `json.dumps` would output.

    SQLAlchemy expects that the json serializer returns `str` and calls
    `.encode()` on the value to turn it to bytes before writing to the
    JSONB column. I'd need to either wrap `orjson.dumps` to return a
    `str` so that SQLAlchemy could then convert it to binary, or do the
    following, which changes the behaviour of the dialect to expect a
    binary value from the serializer.

    See Also:
    https://github.com/sqlalchemy/sqlalchemy/blob/14bfbadfdf9260a1c40f63b31641b27fe9de12a0/lib/sqlalchemy/dialects/postgresql/asyncpg.py#L934
    """

    def encoder(bin_value: bytes) -> bytes:
        # \x01 is the prefix for jsonb used by PostgreSQL.
        # asyncpg requires it when format='binary'
        return b"\x01" + bin_value

    def decoder(bin_value: bytes) -> Any:
        # the byte is the \x01 prefix for jsonb used by PostgreSQL.
        # asyncpg returns it when format='binary'
        return msgspec.json.decode(bin_value[1:])

    dbapi_connection.await_(
        dbapi_connection.driver_connection.set_type_codec(
            "jsonb",
            encoder=encoder,
            decoder=decoder,
            schema="pg_catalog",
            format="binary",
        )
    )


async def before_send_handler(message: Any, scope: Any) -> None:
    """Custom `before_send_handler` for SQLAlchemy plugin that inspects the
    status of response and commits, or rolls back the database.

    Args:
        message: ASGI message
        _:
        scope: ASGI scope
    """
    session = cast(
        "AsyncSession | None", get_litestar_scope_state(scope, SESSION_SCOPE_KEY)
    )
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
    [index, get_account_types],
    dependencies={"transaction": provide_transaction},
    plugins=[SQLAlchemyPlugin(_db_config)],
)


def Maple() -> Litestar:
    return __app
