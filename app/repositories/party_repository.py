"""
Party Repository.

Database access layer
for Party Management.
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.party import Party


class PartyRepository:
    """Repository for Party."""

    def __init__(
        self,
        db: Session,
    ) -> None:
        self.db = db

    def create(
        self,
        party: Party,
    ) -> Party:
        """
        Create new party.
        """

        self.db.add(party)
        self.db.commit()
        self.db.refresh(party)

        return party

    def get_by_id(
        self,
        party_id: int,
    ) -> Party | None:
        """
        Get party by ID.
        """

        return (
            self.db.query(Party)
            .filter(
                Party.id == party_id,
                Party.is_active.is_(True),
            )
            .first()
        )

    def get_all(
        self,
    ) -> list[Party]:
        """
        Get all active parties.
        """

        return (
            self.db.query(Party)
            .filter(
                Party.is_active.is_(True),
            )
            .order_by(
                Party.party_name,
            )
            .all()
        )



    




    def update(
        self,
        party_id: int,
        party_data: dict,
    ) -> Party | None:
        """
        Update existing party.
        """

        party = self.get_by_id(
            party_id,
        )

        if party is None:
            return None

        for key, value in party_data.items():
            if hasattr(
                party,
                key,
            ):
                setattr(
                    party,
                    key,
                    value,
                )

        self.db.commit()
        self.db.refresh(
            party,
        )

        return party

    def soft_delete(
        self,
        party_id: int,
    ) -> bool:
        """
        Soft delete party.
        """

        party = self.get_by_id(
            party_id,
        )

        if party is None:
            return False

        party.is_active = False

        self.db.commit()
        self.db.refresh(
            party,
        )

        return True

    def exists_by_name(
        self,
        party_name: str,
    ) -> bool:
        """
        Check duplicate party name.
        """

        return (
            self.db.query(Party)
            .filter(
                Party.party_name == party_name,
                Party.is_active.is_(True),
            )
            .first()
            is not None
        )







    def exists_by_mobile(
        self,
        mobile: str,
    ) -> bool:
        """
        Check duplicate mobile.
        """

        return (
            self.db.query(Party)
            .filter(
                Party.mobile == mobile,
                Party.is_active.is_(True),
            )
            .first()
            is not None
        )

    def search(
        self,
        keyword: str,
    ) -> list[Party]:
        """
        Search party by name, mobile or email.
        """

        return (
            self.db.query(Party)
            .filter(
                Party.is_active.is_(True),
                or_(
                    Party.party_name.ilike(
                        f"%{keyword}%"
                    ),
                    Party.mobile.ilike(
                        f"%{keyword}%"
                    ),
                    Party.email.ilike(
                        f"%{keyword}%"
                    ),
                ),
            )
            .order_by(
                Party.party_name,
            )
            .all()
        )