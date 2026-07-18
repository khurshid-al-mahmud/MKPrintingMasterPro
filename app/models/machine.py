"""
Machine Master Model.

Stores every Printing Machine
used inside the Printing ERP.

Supports both:

- Offset Printing
- Digital Printing
"""

from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base


class Machine(Base):
    """Machine Master."""

    __tablename__ = "machines"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    machine_code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )

    machine_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    machine_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    manufacturer: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    model: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    max_sheet_size: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    max_print_width: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )

    max_print_length: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )

    color_capacity: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    production_speed: Mapped[int | None] = mapped_column(
        nullable=True,
    )

    hourly_running_cost: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=Decimal("0.00"),
        nullable=False,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
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