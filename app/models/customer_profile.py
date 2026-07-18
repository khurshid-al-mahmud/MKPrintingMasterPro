"""
Customer Profile Model.

Stores customer-specific information.

Every Customer Profile belongs to one Party.
"""

from decimal import Decimal

from sqlalchemy import Boolean, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class CustomerProfile(Base):
    """Customer Profile."""

    __tablename__ = "customer_profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    party_id: Mapped[int] = mapped_column(
        ForeignKey(
            "parties.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
        index=True,
    )

    customer_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    customer_category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    credit_limit: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    credit_days: Mapped[int] = mapped_column(
        default=0,
        nullable=False,
    )

    price_category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    discount_rate: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    party = relationship(
        "Party",
        back_populates="customer_profile",
    )