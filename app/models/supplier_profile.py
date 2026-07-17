"""
Supplier Profile Model.

Stores supplier-specific information.

Every Supplier Profile belongs to one Party.
"""

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.models.base import Base


class SupplierProfile(Base):
    """Supplier Profile."""

    __tablename__ = "supplier_profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    party_id: Mapped[int] = mapped_column(
        ForeignKey("parties.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    supplier_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    supplier_category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    payment_terms: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    preferred_supplier: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )