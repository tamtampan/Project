"""Office Model Module"""

from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class Office(Base):
    """Office Model"""

    __tablename__ = "office"
    office_id = Column(String(100), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False, unique=True)
    phone = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    postal_code = Column(String(50), nullable=False)
    territory = Column(String(50), nullable=False)

    def __init__(self, name, phone, address, city, country, postal_code, territory):
        self.name = name
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.territory = territory
