from sqlalchemy import Column, Integer, ForeignKey, Numeric, JSON, DateTime
from sqlalchemy.sql import func
from app.db.session import Base


class OrderProduct(Base):
    __tablename__ = "order_products"

    id = Column(Integer, primary_key=True, index=True)
    orderId = Column(Integer, ForeignKey("orders.id"), nullable=False)
    productId = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    extras = Column(JSON, nullable=True)  # Detalles de los extras en formato JSON
    finalPrice = Column(Numeric(10, 2), nullable=False)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, onupdate=func.now())
