from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Numeric,
    JSON,
    DateTime,
    CheckConstraint,
)
from sqlalchemy.sql import func
from app.db.session import Base
from sqlalchemy.orm import relationship


class OrderProduct(Base):
    __tablename__ = "order_products"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    extras = Column(JSON, nullable=True)  # Detalles de los extras en formato JSON
    final_price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    order = relationship("Order", back_populates="order_products")
    product = relationship("Product", back_populates="order_products")

    __table_args__ = (
        CheckConstraint("quantity > 0", name="check_quantity_positive"),
        CheckConstraint("final_price >= 0", name="check_final_price_non_negative"),
    )
