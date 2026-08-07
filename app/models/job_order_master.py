"""
MKPrintingMasterPro ERP

Job Order Master Model

Stores Job Order header information.
Build-030
"""

from datetime import date
from datetime import datetime

from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class JobOrderMaster(Base):
    """
    Job Order Master.
    """

    __tablename__ = "job_order_master"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    job_order_no: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    job_order_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    invoice_id: Mapped[int] = mapped_column(
        ForeignKey("invoice_masters.id"),
        nullable=False,
        index=True,
    )

    quotation_id: Mapped[int | None] = mapped_column(
        ForeignKey("quotation_master.id"),
        nullable=True,
        index=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("parties.id"),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Open",
        nullable=False,
    )

    priority: Mapped[str] = mapped_column(
        String(30),
        default="Normal",
        nullable=False,
    )

    delivery_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    remarks: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
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


    # ==========================
    # Basic Relationships
    # ==========================

    customer = relationship(
        "Party",
    )

    quotation = relationship(
        "QuotationMaster",
    )

    invoice = relationship(
        "InvoiceMaster",
        back_populates="job_orders",
    )


    # ==========================
    # Job Order Items
    # ==========================

    items = relationship(
        "JobOrderItem",
        back_populates="job_order",
        cascade="all, delete-orphan",
    )


    # ==========================
    # Production Order Relationship
    # Build-031
    # ==========================

    production_orders = relationship(
        "ProductionOrderMaster",
        back_populates="job_order",
        cascade="all, delete-orphan",
    )