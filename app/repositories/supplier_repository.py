"""
Supplier Repository.

Database access layer
for Supplier Management.
"""

from sqlalchemy import or_

from app.models.party import Party
from app.models.supplier_profile import SupplierProfile


class SupplierRepository:
    """
    Repository for Supplier Profile.
    """

    def __init__(
        self,
        db,
    ):
        self.db = db

    def create(
        self,
        supplier: SupplierProfile,
    ) -> SupplierProfile:

        self.db.add(
            supplier,
        )

        self.db.commit()

        self.db.refresh(
            supplier,
        )

        return supplier

    def get_by_id(
        self,
        supplier_id: int,
    ) -> SupplierProfile | None:

        return (
            self.db.query(
                SupplierProfile,
            )
            .filter(
                SupplierProfile.id == supplier_id,
                SupplierProfile.is_active == True,
            )
            .first()
        )

    def get_all(
        self,
    ) -> list[SupplierProfile]:

        return (
            self.db.query(
                SupplierProfile,
            )
            .filter(
                SupplierProfile.is_active == True,
            )
            .all()
        )

    def update(
        self,
        supplier_id: int,
        supplier_data: dict,
    ) -> SupplierProfile | None:

        supplier = self.get_by_id(
            supplier_id,
        )

        if supplier is None:
            return None

        for key, value in supplier_data.items():
            setattr(
                supplier,
                key,
                value,
            )

        self.db.commit()

        self.db.refresh(
            supplier,
        )

        return supplier

    def soft_delete(
        self,
        supplier_id: int,
    ) -> bool:

        supplier = self.get_by_id(
            supplier_id,
        )

        if supplier is None:
            return False

        supplier.is_active = False

        self.db.commit()

        return True

    def search(
        self,
        keyword: str,
    ) -> list[SupplierProfile]:

        return (
            self.db.query(
                SupplierProfile,
            )
            .join(
                Party,
                SupplierProfile.party_id == Party.id,
            )
            .filter(
                SupplierProfile.is_active == True,
            )
            .filter(
                or_(
                    Party.party_name.ilike(
                        f"%{keyword}%",
                    ),
                    Party.mobile.ilike(
                        f"%{keyword}%",
                    ),
                )
            )
            .all()
        )