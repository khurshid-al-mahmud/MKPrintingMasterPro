"""
MKPrintingMasterPro ERP

Production Operation Execution Status History

Build-035
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


class ProductionOperationExecutionStatusHistory(Base):
    """
    Records every status change of a production operation execution.
    """

    __tablename__ = "production_operation_execution_status_histories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    production_operation_execution_id: Mapped[int] = mapped_column(
        ForeignKey(
            "production_operation_executions.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    previous_status: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    new_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        index=True,
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

    operator_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )

    production_operation_execution = relationship(
        "ProductionOperationExecution",
        back_populates="production_execution_status_histories",
    )
