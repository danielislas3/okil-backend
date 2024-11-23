from pydantic_settings import BaseSettings
import logging


class Settings(BaseSettings):
    PROJECT_NAME: str = "Cafeteria POS API"
    API_VERSION: str = "/api/v1"
    DATABASE_URL: str
    APP_ENV: str = "development"


class Config:
    env_file = ".env"
    extra = "allow"


settings = Settings()


def configure_logging():
    if settings.APP_ENV == "development":
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


configure_logging()
