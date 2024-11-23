from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(
        Integer, ForeignKey("categories.id"), nullable=False, index=True
    )
    base_price = Column(Numeric(10, 2), nullable=False)
    size = Column(String, nullable=True)
    margin = Column(Numeric(5, 2), nullable=False)
    is_available = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    category = relationship("Category", back_populates="products")
    order_products = relationship("OrderProduct", back_populates="product")
