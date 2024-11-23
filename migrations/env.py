from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde .env
load_dotenv()

# Este es el objeto de configuración de Alembic
config = context.config

# Configurar la URL de la base de datos desde .env
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# Configuración de logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importar modelos y metadata
from app.db.session import Base
from app.models.user import User
from app.models.client import Client  # Importar modelo Client
from app.models import category, product, product_extra, order, order_product, coupon

# Configurar target_metadata
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecutar migraciones en modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecutar migraciones en modo 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
