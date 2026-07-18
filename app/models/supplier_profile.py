"""
Supplier Profile Model.

ERP Supplier Information.
"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class SupplierProfile(BaseModel):
    """
    Supplier profile table.
    """

    __tablename__ = "supplier_profiles"

    party_id: Mapped[int] = mapped_column(
        ForeignKey(
            "parties.id",
            ondelete="CASCADE",
        ),
        unique=True,
        nullable=False,
    )

    supplier_code: Mapped[str] = mapped_column(
        unique=True,
        index=True,
    )

    trade_license: Mapped[str | None]

    vat_number: Mapped[str | None]

    tin_number: Mapped[str | None]

    credit_limit: Mapped[float] = mapped_column(
        default=0,
    )

    current_balance: Mapped[float] = mapped_column(
        default=0,
    )

    party = relationship(
        "Party",
        back_populates="supplier_profile",
    )