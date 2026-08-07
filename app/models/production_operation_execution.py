"""
MKPrintingMasterPro ERP

Production Operation Execution Model

Build-034

Tracks actual execution progress of assigned production operations.
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class ProductionOperationExecution(Base):
    """
    Actual execution record of a production operation.
    """

    __tablename__ = "production_operation_executions"

    # ==========================
    # Primary Key
    # ==========================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    # ==========================
    # Production Order
    # ==========================

    production_order_id: Mapped[int] = mapped_column(
        ForeignKey(
            "production_order_masters.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==========================
    # Operation Assignment
    # ==========================

    operation_assignment_id: Mapped[int] = mapped_column(
        ForeignKey(
            "operation_assignments.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==========================
    # Execution Status
    # ==========================

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Pending",
        index=True,
    )

    # ==========================
    # Quantity
    # ==========================

    planned_quantity: Mapped[float | None] = mapped_column(
        Numeric(18, 3),
        nullable=True,
    )

    completed_quantity: Mapped[float | None] = mapped_column(
        Numeric(18, 3),
        nullable=True,
        default=0,
    )

    reject_quantity: Mapped[float | None] = mapped_column(
        Numeric(18, 3),
        nullable=True,
        default=0,
    )

    # ==========================
    # Actual Time
    # ==========================

    actual_start_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    actual_end_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # ==========================
    # Operator
    # ==========================

    operator_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # ==========================
    # Remarks
    # ==========================

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ==========================
    # Audit
    # ==========================

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
    # Relationships
    # ==========================

    production_order = relationship(
        "ProductionOrderMaster",
        back_populates="operation_executions",
    )

    operation_assignment = relationship(
        "OperationAssignment",
        back_populates="production_operation_executions",
    )

    # Build-034
    # Production Output Tracking

    production_outputs = relationship(
        "ProductionOutput",
        back_populates="production_operation_execution",
        cascade="all, delete-orphan",
    )