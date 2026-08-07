"""
MKPrintingMasterPro ERP

Quotation Item Model

Phase-9
Build-002
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    DateTime,
    ForeignKey,
    Text,
)

from sqlalchemy.orm import relationship

from app.models.base import Base


class QuotationItem(Base):

    __tablename__ = "quotation_items"


    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )


    quotation_id = Column(
        Integer,
        ForeignKey("quotation_master.id"),
        nullable=False,
    )


    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
    )


    description = Column(
        Text,
        nullable=True,
    )


    quantity = Column(
        Numeric(18, 2),
        nullable=False,
        default=1,
    )


    unit = Column(
        String(30),
        nullable=True,
    )


    unit_price = Column(
        Numeric(18, 2),
        nullable=False,
        default=0,
    )


    amount = Column(
        Numeric(18, 2),
        nullable=False,
        default=0,
    )


    specification = Column(
        Text,
        nullable=True,
    )


    remarks = Column(
        Text,
        nullable=True,
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


    quotation = relationship(
        "QuotationMaster",
        back_populates="items",
    )


    product = relationship(
        "Product",
    )