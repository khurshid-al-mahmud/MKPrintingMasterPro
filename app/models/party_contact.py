"""
Party Contact Model.

Stores multiple contact persons
for a Party.

Example:

ABC Traders

- Rahim
- Karim
- Hasan
"""

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)

from app.models.base import Base


class PartyContact(Base):
    """Party Contact Person."""

    __tablename__ = "party_contacts"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    party_id = Column(
        Integer,
        ForeignKey("parties.id"),
        nullable=False,
        index=True,
    )

    contact_name = Column(
        String(200),
        nullable=False,
    )

    designation = Column(
        String(150),
        nullable=True,
    )

    mobile = Column(
        String(20),
        nullable=True,
    )

    alternate_mobile = Column(
        String(20),
        nullable=True,
    )

    email = Column(
        String(150),
        nullable=True,
    )

    notes = Column(
        Text,
        nullable=True,
    )

    is_primary = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )