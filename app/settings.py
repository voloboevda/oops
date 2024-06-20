from pydantic_settings import BaseSettings
import logging

logger = logging.getLogger(__name__)

class Settings(BaseSettings): 
    db_username: str
    db_name: str
    db_password: str
    db_host: str
    db_port: int

    def get_pg_dsn(self) -> str:
        return f"postgres://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

def get_service_settings() -> Settings:
    try:
        import dotenv  # noqa

        dotenv.load_dotenv()
        logger.info(".env file imported")
    except ImportError:  # pragma: no cover
        logger.info(".env file won't be imported")
    return Settings()


settings = get_service_settings()
