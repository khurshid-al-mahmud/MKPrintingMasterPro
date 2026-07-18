"""
Supplier Service.

Business Logic Layer
for Supplier Management.
"""

from app.models.supplier_profile import SupplierProfile
from app.repositories.supplier_repository import SupplierRepository
from app.schemas.supplier import (
    SupplierCreate,
    SupplierUpdate,
)


class SupplierService:
    """
    Service layer for Supplier management.
    """

    def __init__(
        self,
        repository: SupplierRepository,
    ) -> None:
        self.repository = repository

    def create(
        self,
        supplier: SupplierCreate,
    ) -> SupplierProfile:
        """
        Create supplier.
        """

        new_supplier = SupplierProfile(
            party_id=supplier.party_id,
            supplier_code=supplier.supplier_code,
            trade_license=supplier.trade_license,
            vat_number=supplier.vat_number,
            tin_number=supplier.tin_number,
            credit_limit=supplier.credit_limit,
            current_balance=supplier.current_balance,
        )

        return self.repository.create(
            new_supplier,
        )

    def get_by_id(
        self,
        supplier_id: int,
    ) -> SupplierProfile | None:
        """
        Get supplier by ID.
        """

        return self.repository.get_by_id(
            supplier_id,
        )

    def get_all(
        self,
    ) -> list[SupplierProfile]:
        """
        Get all suppliers.
        """

        return self.repository.get_all()

    def update(
        self,
        supplier_id: int,
        supplier_data: SupplierUpdate,
    ) -> SupplierProfile | None:
        """
        Update supplier.
        """

        return self.repository.update(
            supplier_id,
            supplier_data.model_dump(
                exclude_unset=True,
            ),
        )

    def delete(
        self,
        supplier_id: int,
    ) -> bool:
        """
        Soft delete supplier.
        """

        return self.repository.soft_delete(
            supplier_id,
        )

    def search(
        self,
        keyword: str,
    ) -> list[SupplierProfile]:
        """
        Search suppliers.
        """

        return self.repository.search(
            keyword,
        )