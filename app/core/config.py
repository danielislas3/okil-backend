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
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_level = logging.DEBUG if settings.is_development else logging.INFO

    # Configure root logger
    logging.basicConfig(
        level=log_level,
        format=log_format
    )

    if not settings.is_development:
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler(
            'app.log',
            maxBytes=1024 * 1024,  # 1MB
            backupCount=5
        )
        file_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(file_handler)

    # Suppress noisy loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)


configure_logging()
