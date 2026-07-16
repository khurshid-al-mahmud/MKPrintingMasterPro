"""
Supplier Profile Model.

Stores supplier-specific information.

Every Supplier Profile belongs to one Party.
"""

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)

from app.models.base import Base


class SupplierProfile(Base):
    """Supplier Profile."""

    __tablename__ = "supplier_profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    party_id = Column(
        Integer,
        ForeignKey("parties.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    supplier_number = Column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    supplier_category = Column(
        String(100),
        nullable=True,
    )

    payment_terms = Column(
        String(200),
        nullable=True,
    )

    preferred_supplier = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )