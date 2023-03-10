"""Office Repository"""

from sqlalchemy.orm import Session

from app.offices.models import Office


class OfficeRepository:
    """Office Repository"""

    def __init__(self, db: Session):
        self.db = db

    def create(
        self, name: str, phone: str, address: str, city: str, country: str, postal_code: str, territory: str
    ) -> object:
        """Create Office"""

        try:
            office = Office(name, phone, address, city, country, postal_code, territory)
            self.db.add(office)
            self.db.commit()
            self.db.refresh(office)
            return office
        except Exception as exc:
            raise exc

    def read_by_id(self, office_id: str) -> object:
        """Read by id"""

        try:
            office = self.db.query(Office).filter(Office.office_id == office_id).first()
            return office
        except Exception as exc:
            raise exc

    def read_all(self) -> list[object]:
        """Read all"""

        try:
            offices = self.db.query(Office).all()
            return offices
        except Exception as exc:
            raise exc

    def delete_by_id(self, office_id: str) -> bool or None:
        """Delete by id"""

        try:
            office = self.db.query(Office).filter(Office.office_id == office_id).first()
            if office is None:
                return None
            self.db.delete(office)
            self.db.commit()
            return True
        except Exception as exc:
            raise exc

    def update(
        self,
        office_id: str,
        name: str = None,
        phone: str = None,
        address: str = None,
        city: str = None,
        country: str = None,
        postal_code: str = None,
        territory: str = None,
    ) -> object:
        """Update"""

        try:
            office = self.db.query(Office).filter(Office.office_id == office_id).first()
            if office is None:
                return None
            if name is not None:
                office.name = name
            if phone is not None:
                office.phone = phone
            if address is not None:
                office.address = address
            if city is not None:
                office.city = city
            if country is not None:
                office.country = country
            if postal_code is not None:
                office.postal_code = postal_code
            if territory is not None:
                office.territory = territory
            self.db.add(office)
            self.db.commit()
            self.db.refresh(office)
            return office
        except Exception as exc:
            raise exc

    def read_by_name(self, name: str) -> object:
        """Read by name"""

        try:
            office = self.db.query(Office).filter(Office.name.ilike(f"{name}%")).first()
            if office is None:
                return None
            return office
        except Exception as exc:
            raise exc
