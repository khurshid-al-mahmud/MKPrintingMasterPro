"""
Print Partner Service.

Business logic
for Print Partner Management.
"""

from fastapi import HTTPException

from app.repositories.print_partner_repository import (
    PrintPartnerRepository,
)
from app.schemas.print_partner import (
    PrintPartnerCreate,
    PrintPartnerUpdate,
)


class PrintPartnerService:
    """
    Service layer for Print Partner.
    """

    def __init__(
        self,
        repository: PrintPartnerRepository,
    ):
        self.repository = repository


    def get_all(self):
        """
        Get all print partners.
        """

        return self.repository.get_all()


    def get_by_id(
        self,
        partner_id: int,
    ):
        """
        Get print partner by ID.
        """

        partner = self.repository.get_by_id(
            partner_id
        )

        if not partner:
            raise HTTPException(
                status_code=404,
                detail="Print Partner not found.",
            )

        return partner


    def create(
        self,
        partner: PrintPartnerCreate,
    ):
        """
        Create print partner.
        """

        if self.repository.exists_by_code(
            partner.partner_code
        ):
            raise HTTPException(
                status_code=400,
                detail="Partner code already exists.",
            )


        return self.repository.create(
            partner.model_dump()
        )


    def update(
        self,
        partner_id: int,
        partner: PrintPartnerUpdate,
    ):
        """
        Update print partner.
        """

        data = partner.model_dump(
            exclude_unset=True
        )


        return self.repository.update(
            partner_id,
            data,
        )


    def delete(
        self,
        partner_id: int,
    ):
        """
        Delete print partner.
        """

        return self.repository.delete(
            partner_id
        )


    def search(
        self,
        keyword: str,
    ):
        """
        Search print partner.
        """

        return self.repository.search(
            keyword
        )