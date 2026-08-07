"""
MKPrintingMasterPro ERP

Quotation Master Model

Phase-9
Build-001
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Numeric,
    ForeignKey,
    Text,
)

from sqlalchemy.orm import relationship

from app.models.base import Base


class QuotationMaster(Base):

    __tablename__ = "quotation_master"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    quotation_no = Column(
        String(50),
        unique=True,
        nullable=False,
    )

    quotation_date = Column(
        Date,
        nullable=False,
    )

    customer_id = Column(
        Integer,
        ForeignKey("parties.id"),
        nullable=False,
    )

    contact_person = Column(
        String(200),
        nullable=True,
    )

    validity_days = Column(
        Integer,
        default=30,
    )

    status = Column(
        String(30),
        default="Draft",
    )

    remarks = Column(
        Text,
        nullable=True,
    )

    subtotal = Column(
        Numeric(18, 2),
        default=0,
    )

    discount_amount = Column(
        Numeric(18, 2),
        default=0,
    )

    vat_amount = Column(
        Numeric(18, 2),
        default=0,
    )

    tax_amount = Column(
    Numeric(18, 2),
    default=0,
    )

    grand_total = Column(
        Numeric(18, 2),
        default=0,
    )

    created_by = Column(
        String(100),
        default="system",
    )

    updated_by = Column(
        String(100),
        default="system",
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    customer = relationship(
        "Party",
    )

    items = relationship(
    "QuotationItem",
    back_populates="quotation",
    cascade="all, delete-orphan",
)