"""
Party Repository.

Handles all Party database operations.

This Repository will be used by:

- Customer Module
- Supplier Module
- Employee Module
- Sales Module
- Purchase Module
"""

from typing import Optional

from sqlalchemy.orm import Session

from app.models.party import Party


class PartyRepository:
    """Repository for Party operations."""

    def __init__(self, db: Session):
        self.db = db

    # ----------------------------------------
    # CREATE
    # ----------------------------------------

    def create(self, party: Party) -> Party:
        """Create new Party."""
        self.db.add(party)
        self.db.commit()
        self.db.refresh(party)
        return party

    # ----------------------------------------
    # GET BY ID
    # ----------------------------------------

    def get_by_id(
        self,
        party_id: int,
    ) -> Optional[Party]:
        """Get Party by ID."""
        return (
            self.db.query(Party)
            .filter(
                Party.id == party_id,
                Party.is_active.is_(True),
            )
            .first()
        )

    # ----------------------------------------
    # GET ALL
    # ----------------------------------------

    def get_all(self):
        """Get all active parties."""
        return (
            self.db.query(Party)
            .filter(
                Party.is_active.is_(True),
            )
            .order_by(Party.party_name)
            .all()
        )

    # ----------------------------------------
    # GET BY MOBILE
    # ----------------------------------------

    def get_by_mobile(
        self,
        mobile: str,
    ) -> Optional[Party]:
        """Get Party by primary mobile."""
        return (
            self.db.query(Party)
            .filter(
                Party.mobile == mobile,
                Party.is_active.is_(True),
            )
            .first()
        )

    # ----------------------------------------
    # UPDATE
    # ----------------------------------------

    def update(
        self,
        party: Party,
    ) -> Party:
        """Update Party."""
        self.db.commit()
        self.db.refresh(party)
        return party

    # ----------------------------------------
    # DEACTIVATE
    # ----------------------------------------

    def deactivate(
        self,
        party: Party,
    ) -> Party:
        """Soft delete (Inactive)."""
        party.is_active = False

        self.db.commit()
        self.db.refresh(party)

        return party

    # ----------------------------------------
    # DUPLICATE CHECK
    # ----------------------------------------

    def exists_by_mobile(
        self,
        mobile: str,
    ) -> bool:
        """Check duplicate mobile."""
        return (
            self.db.query(Party)
            .filter(
                Party.mobile == mobile,
                Party.is_active.is_(True),
            )
            .first()
            is not None
        )

    def exists_by_name(
        self,
        party_name: str,
    ) -> bool:
        """Check duplicate party name."""
        return (
            self.db.query(Party)
            .filter(
                Party.party_name == party_name,
                Party.is_active.is_(True),
            )
            .first()
            is not None
        )