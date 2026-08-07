"""
MKPrintingMasterPro ERP

Operation Master

Build-032
"""

from datetime import datetime

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base


class OperationMaster(Base):
    """
    Reusable production operation master.

    Examples:
        Design
        Printing
        Lamination
        Die Cutting
        Foiling
        Spot UV
        Creasing
        Emboss
        Binding
        Sewing
        Perforation

    Operations are later assigned dynamically to
    Work Order Sections.
    """

    __tablename__ = "operation_masters"

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
    # Operation Code
    # ==========================

    operation_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    # ==========================
    # Operation Name
    # ==========================

    operation_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    # ==========================
    # Description
    # ==========================

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    # ==========================
    # Display Order
    # ==========================

    display_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    # ==========================
    # Active Status
    # ==========================

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
    )

    # ==========================
    # Audit Fields
    # ==========================

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
    # Operation Assignment
    # Build-032 Phase-2
    # ==========================

    operation_assignments = relationship(
        "OperationAssignment",
        back_populates="operation",
        cascade="all, delete-orphan",
        order_by="OperationAssignment.sequence_no",
    )