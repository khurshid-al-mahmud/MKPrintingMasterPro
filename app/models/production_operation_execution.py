"""
MKPrintingMasterPro ERP

Production Operation Execution Model

Build-034 + Build-035
"""

from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base import Base


class ProductionOperationExecution(Base):
    """
    Actual execution record of a production operation.

    Build-034:
        Core execution tracking.

    Build-035:
        Execution history and status history relationships.
    """

    __tablename__ = "production_operation_executions"

    # ==================================================
    # Primary Key
    # ==================================================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    # ==================================================
    # Production Order
    # ==================================================

    production_order_id: Mapped[int] = mapped_column(
        ForeignKey(
            "production_order_masters.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==================================================
    # Operation Assignment
    # ==================================================

    operation_assignment_id: Mapped[int] = mapped_column(
        ForeignKey(
            "operation_assignments.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==================================================
    # Execution Status
    # ==================================================

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Pending",
        index=True,
    )

    # ==================================================
    # Quantity
    # ==================================================

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

    # ==================================================
    # Actual Time
    # ==================================================

    actual_start_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    actual_end_time: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # ==================================================
    # Operator
    # ==================================================

    operator_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    # ==================================================
    # Remarks
    # ==================================================

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ==================================================
    # Audit
    # ==================================================

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

    # ==================================================
    # Relationships
    # ==================================================

    production_order = relationship(
        "ProductionOrderMaster",
        back_populates="operation_executions",
    )

    operation_assignment = relationship(
        "OperationAssignment",
        back_populates="production_operation_executions",
    )

    production_outputs = relationship(
        "ProductionOutput",
        back_populates="production_operation_execution",
        cascade="all, delete-orphan",
    )

    # Build-035
    production_execution_histories = relationship(
        "ProductionOperationExecutionHistory",
        back_populates="production_operation_execution",
        cascade="all, delete-orphan",
        order_by="ProductionOperationExecutionHistory.id",
    )

    # Build-035
    production_execution_status_histories = relationship(
        "ProductionOperationExecutionStatusHistory",
        back_populates="production_operation_execution",
        cascade="all, delete-orphan",
        order_by="ProductionOperationExecutionStatusHistory.id",
    )
