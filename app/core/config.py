from pydantic_settings import BaseSettings
import logging


class Settings(BaseSettings):
    PROJECT_NAME: str = "Cafeteria POS API"
    API_VERSION: str = "/api/v1"
    DATABASE_URL: str
    APP_ENV: str = "development"

    @property
    def is_development(self) -> bool:
        return self.APP_ENV.lower() == "development"

    class Config:
        env_file = ".env"
        extra = "allow"


def get_settings() -> Settings:
    try:
        return Settings()
    except Exception as e:
        logging.error(f"Failed to load settings: {e}")
        raise


settings = get_settings()


def configure_logging():
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_level = logging.DEBUG if settings.is_development else logging.INFO

    # Configure root logger
    logging.basicConfig(level=log_level, format=log_format)

    if not settings.is_development:
        from logging.handlers import RotatingFileHandler

        file_handler = RotatingFileHandler(
            "app.log", maxBytes=1024 * 1024, backupCount=5  # 1MB
        )
        file_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger().addHandler(file_handler)

    # Suppress noisy loggers
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)


configure_logging()
