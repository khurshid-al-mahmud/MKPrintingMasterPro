"""
Company Profile Model.

Stores company information
for the ERP owner.
"""

from sqlalchemy import Boolean
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import BaseModel


class CompanyProfile(BaseModel):
    """
    Company Profile.
    """

    __tablename__ = "company_profiles"

    company_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    company_name_en: Mapped[str] = mapped_column(
        String(200),
        nullable=True,
    )

    logo_path: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    mobile: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    website: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True,
    )

    facebook: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True,
    )

    trade_license: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    bin_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    tin_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    vat_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    bank_name: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    bank_account_name: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    bank_account_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    bank_branch: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    confidential_visible: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
