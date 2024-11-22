from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    categoryId = Column(Integer, ForeignKey("categories.id"), nullable=False)
    basePrice = Column(Numeric(10, 2), nullable=False)
    size = Column(String, nullable=True)
    margin = Column(Numeric(5, 2), nullable=False)
    isAvailable = Column(Boolean, default=True)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, onupdate=func.now())

    category = relationship("Category", back_populates="products")
