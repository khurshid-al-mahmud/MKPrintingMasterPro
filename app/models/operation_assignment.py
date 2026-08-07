"""
MKPrintingMasterPro ERP

Operation Assignment Model

Build-032 + Build-033

Assigns individual production operations and tracks execution.
"""

from datetime import date, datetime

from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import UniqueConstraint

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class OperationAssignment(Base):
    """
    Assign a production operation to a responsible party.
    """

    __tablename__ = "operation_assignments"

    __table_args__ = (
        UniqueConstraint(
            "production_order_id",
            "operation_id",
            "sequence_no",
            name="uq_operation_assignment_order_operation_sequence",
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    production_order_id: Mapped[int] = mapped_column(
        ForeignKey(
            "production_order_masters.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    operation_id: Mapped[int] = mapped_column(
        ForeignKey(
            "operation_masters.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
        index=True,
    )

    sequence_no: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
        index=True,
    )

    assigned_party_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "parties.id",
            ondelete="SET NULL",
        ),
        nullable=True,
        index=True,
    )

    assigned_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Internal",
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Pending",
        index=True,
    )

    is_required: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
    )

    is_completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    planned_start_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    planned_end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    instructions: Mapped[str | None] = mapped_column(
        Text,
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
    # Relationships
    # ==========================

    production_order = relationship(
        "ProductionOrderMaster",
        back_populates="operation_assignments",
    )


    operation = relationship(
        "OperationMaster",
        back_populates="operation_assignments",
    )


    assigned_party = relationship(
        "Party",
        foreign_keys=[assigned_party_id],
    )


    # Build-033
    production_operation_executions = relationship(
        "ProductionOperationExecution",
        back_populates="operation_assignment",
        cascade="all, delete-orphan",
    )