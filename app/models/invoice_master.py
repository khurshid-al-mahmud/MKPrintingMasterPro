"""
Invoice Master Model.

Stores invoice header information.
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class InvoiceMaster(Base):
    """Invoice Master."""

    __tablename__ = "invoice_masters"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    invoice_no: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    invoice_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("parties.id"),
        nullable=False,
        index=True,
    )

    quotation_id: Mapped[int | None] = mapped_column(
        ForeignKey("quotation_master.id"),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Draft",
        nullable=False,
    )

    remarks: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    subtotal: Mapped[float] = mapped_column(
        Float,
        default=0,
        nullable=False,
    )

    discount_amount: Mapped[float] = mapped_column(
        Float,
        default=0,
        nullable=False,
    )

    vat_amount: Mapped[float] = mapped_column(
        Float,
        default=0,
        nullable=False,
    )

    tax_amount: Mapped[float] = mapped_column(
        Float,
        default=0,
        nullable=False,
    )

    grand_total: Mapped[float] = mapped_column(
        Float,
        default=0,
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

    customer = relationship(
        "Party",
    )

    quotation = relationship(
        "QuotationMaster",
    )

    items = relationship(
        "InvoiceItem",
        back_populates="invoice",
        cascade="all, delete-orphan",
    )

    job_orders = relationship(
        "JobOrderMaster",
        back_populates="invoice",
    )