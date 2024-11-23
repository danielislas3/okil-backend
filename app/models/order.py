from sqlalchemy import Column, Integer, Numeric, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base
import enum


class PaymentMethod(enum.Enum):
    cash = "cash"
    card = "card"


class OrderStatus(enum.Enum):
    pending = "pending"
    completed = "completed"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    clientId = Column(Integer, ForeignKey("clients.id"), nullable=True)
    baristaId = Column(Integer, ForeignKey("users.id"), nullable=False)
    totalPrice = Column(Numeric(10, 2), nullable=False)
    discount = Column(Numeric(10, 2), default=0)
    paymentMethod = Column(Enum(PaymentMethod), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    paidAt = Column(DateTime, nullable=True)
    createdAt = Column(DateTime, server_default=func.now())
    updatedAt = Column(DateTime, onupdate=func.now())

    barista = relationship("User", back_populates="orders")
    client = relationship("Client", back_populates="orders")
