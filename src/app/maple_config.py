from dataclasses import dataclass
import os


@dataclass(init=False, frozen=True)
class MapleConfig:
    db_host: str = os.environ['MAPLE_DB_HOST']
    db_user: str = os.environ['MAPLE_DB_USER']
    db_password_key: str = 'MAPLE_DB_PASS'
    db_port: int = int(os.getenv('MAPLE_DB_PORT', 5432))
    db_name: str = os.getenv('MAPLE_DB_DBNAME', 'maple')
    db_search_schema: str = os.getenv('MAPLE_DB_SEARCH_PATH', 'maple')
    db_pool_size: int = int(os.getenv('MAPLE_DB_POOL_SIZE', 5))
    db_max_oveflow: int = int(os.getenv('MAPLE_DB_MAX_OVERFLOW', 10))
    db_pool_timeout: int = int(os.getenv('MAPLE_DB_POOL_TIMEOUT', 30))
    db_echo: bool = bool(int(os.getenv('MAPLE_DB_ECHO', 0)))
    db_echo_pool: bool = bool(int(os.getenv('MAPLE_DB_ECHO_POOL', 0)))
    db_pool_disable: bool = bool(int(os.getenv('MAPLE_DB_POOL_DISABLE', 0)))
    log_level: str = os.getenv('MAPLE_LOG_LEVEL', 'DEBUG')

