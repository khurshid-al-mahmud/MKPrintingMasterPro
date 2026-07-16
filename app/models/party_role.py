"""
Party Role Model.

A Party can have one or more business roles.

Example:

ABC Traders
    ├── Trade Customer
    ├── Supplier

Abdul Karim
    ├── Customer
    ├── Supplier
    └── Employee
"""

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)

from app.models.base import Base


class PartyRole(Base):
    """Party Business Role."""

    __tablename__ = "party_roles"

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

    role = Column(
        String(50),
        nullable=False,
        index=True,
    )

    role_number = Column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )