"""Shopping Cart Model"""

from uuid import uuid4

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db import Base


class ShoppingCart(Base):
    """Shopping Cart Model"""

    __tablename__ = "shopping_cart"
    shopping_cart_id = Column(String(100), primary_key=True, default=uuid4)
    total_cost = Column(Float, default=0)

    customer_id = Column(String(100), ForeignKey("customer.customer_id"), unique=True, nullable=False)
    customer = relationship("Customer", lazy="subquery")

    def __init__(self, customer_id, total_cost=0):
        self.customer_id = customer_id
        self.total_cost = total_cost
