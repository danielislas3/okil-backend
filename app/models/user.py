from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base class for SQLAlchemy models
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    orders = relationship("Order", back_populates="barista")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"
