from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime
from sqlalchemy.sql import func
from app.db.session import Base


class ProductExtra(Base):
    __tablename__ = "product_extras"

    id = Column(Integer, primary_key=True, index=True)
    productId = Column(Integer, ForeignKey("products.id"), nullable=False)
    name = Column(String, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    isAvailable = Column(Boolean, default=True)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, onupdate=func.now())
