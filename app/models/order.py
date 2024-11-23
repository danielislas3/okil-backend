from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Numeric,
    Enum,
    DateTime,
    func,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from app.db.session import Base
import enum


class PaymentMethod(enum.Enum):
    cash = "cash"
    card = "card"


class OrderStatus(enum.Enum):
    """Enum representing the order lifecycle states.

    Normal flow: pending -> preparing -> ready -> completed
    Cancel flow: pending/preparing -> cancelled
    """

    pending = "pending"
    preparing = "preparing"
    ready = "ready"
    completed = "completed"
    cancelled = "cancelled"
    refunded = "refunded"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(
        Integer, ForeignKey("clients.id"), nullable=True, index=True
    )  # Relación con tabla 'clients'
    barista_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    total_price = Column(
        Numeric(10, 2), CheckConstraint("total_price >= 0"), nullable=False
    )
    discount = Column(Numeric(10, 2), CheckConstraint("discount >= 0"), default=0)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    paid_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    client = relationship("Client", back_populates="orders")
    barista = relationship("User", back_populates="orders")
    order_products = relationship("OrderProduct", back_populates="order")
    products = relationship(
        "OrderProduct", back_populates="order", cascade="all, delete-orphan"
    )
