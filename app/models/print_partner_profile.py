"""
Print Partner Profile Model.

Stores print partner specific information.

Every Print Partner Profile belongs to one Party.
"""

from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class PrintPartnerProfile(Base):
    """
    Print Partner Profile.
    """

    __tablename__ = "print_partner_profiles"


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


    partner_code: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )


    specialization: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )


    machine_type: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )


    commission_rate: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        default=Decimal("0.00"),
        nullable=False,
    )


    payment_terms: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


    party = relationship(
        "Party",
        back_populates="print_partner_profile",
    )