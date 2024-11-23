from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está definido. Verifica tu archivo .env")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from app.models.user import User
from app.models.order import Order
from app.models.client import Client
from app.models.category import Category
from app.models.product import Product
from app.models.order_product import OrderProduct


def test_connection():
    try:
        with engine.connect() as connection:
            print("Conexión exitosa a la base de datos")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")


test_connection()
