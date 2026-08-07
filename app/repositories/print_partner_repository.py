"""
Print Partner Repository.

Database access layer
for Print Partner Management.
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.party import Party
from app.models.print_partner_profile import PrintPartnerProfile


class PrintPartnerRepository:
    """
    Repository for Print Partner Profile.
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db


    def create(
        self,
        partner_data: dict,
    ) -> PrintPartnerProfile:
        """
        Create new print partner.
        """

        # Check Party exists
        party = (
            self.db.query(Party)
            .filter(
                Party.id == partner_data["party_id"]
            )
            .first()
        )

        if party is None:
            raise ValueError(
                "Party ID does not exist."
            )


        partner = PrintPartnerProfile(
            **partner_data
        )


        self.db.add(
            partner
        )

        self.db.commit()


        self.db.refresh(
            partner
        )


        return partner


    def get_by_id(
        self,
        partner_id: int,
    ):
        return (
            self.db.query(
                PrintPartnerProfile
            )
            .filter(
                PrintPartnerProfile.id == partner_id,
                PrintPartnerProfile.is_active == True,
            )
            .first()
        )


    def get_all(
        self,
    ):
        return (
            self.db.query(
                PrintPartnerProfile
            )
            .filter(
                PrintPartnerProfile.is_active == True,
            )
            .all()
        )


    def update(
        self,
        partner_id: int,
        partner_data: dict,
    ):

        partner = self.get_by_id(
            partner_id
        )

        if partner is None:
            return None


        for key, value in partner_data.items():

            setattr(
                partner,
                key,
                value,
            )


        self.db.commit()

        self.db.refresh(
            partner
        )

        return partner


    def delete(
        self,
        partner_id: int,
    ):

        partner = self.get_by_id(
            partner_id
        )

        if partner is None:
            return False


        partner.is_active = False

        self.db.commit()

        return True


    def exists_by_code(
        self,
        partner_code: str,
    ):

        return (
            self.db.query(
                PrintPartnerProfile
            )
            .filter(
                PrintPartnerProfile.partner_code == partner_code
            )
            .first()
            is not None
        )


    def search(
        self,
        keyword: str,
    ):

        return (
            self.db.query(
                PrintPartnerProfile
            )
            .join(
                Party,
                PrintPartnerProfile.party_id == Party.id,
            )
            .filter(
                PrintPartnerProfile.is_active == True,
            )
            .filter(
                or_(
                    Party.party_name.ilike(
                        f"%{keyword}%"
                    ),

                    Party.mobile.ilike(
                        f"%{keyword}%"
                    ),

                    PrintPartnerProfile.partner_code.ilike(
                        f"%{keyword}%"
                    ),
                )
            )
            .all()
        )