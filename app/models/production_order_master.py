"""
MKPrintingMasterPro ERP

Production Order Master

Build-031
"""

from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base import Base


class ProductionOrderMaster(Base):
    """
    Production Order Master.

    One Job Order can generate one or more Production Orders.
    """

    __tablename__ = "production_order_masters"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    production_order_no: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    production_order_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    job_order_id: Mapped[int] = mapped_column(
        ForeignKey("job_order_master.id"),
        nullable=False,
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="Open",
    )

    priority: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Normal",
    )

    planned_start_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    planned_end_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_by: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    updated_by: Mapped[str | None] = mapped_column(
        String(100),
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
    # Job Order Relationship
    # Build-031
    # ==========================

    job_order = relationship(
        "JobOrderMaster",
        back_populates="production_orders",
    )

    # ==========================
    # Operation Assignment
    # Build-031 Phase-2
    # ==========================

    operation_assignments = relationship(
        "OperationAssignment",
        back_populates="production_order",
        cascade="all, delete-orphan",
        order_by="OperationAssignment.sequence_no",
    )