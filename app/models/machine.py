"""
Machine Master Model

Build-012
MKPrintingMasterPro ERP
"""

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Integer,
    Numeric,
    String,
    Text,
)

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy.sql import func

from app.models.base import Base


class Machine(Base):
    __tablename__ = "machines"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
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

    serial_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    asset_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    machine_location: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    operator_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    max_paper_width: Mapped[float | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )

    max_paper_height: Mapped[float | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )

    minimum_gsm: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    maximum_gsm: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    color_capacity: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    printing_speed: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    hourly_running_cost: Mapped[float] = mapped_column(
        Numeric(12, 2),
        default=0,
        nullable=False,
    )

    electric_consumption_kw: Mapped[float | None] = mapped_column(
        Numeric(10, 2),
        nullable=True,
    )

    purchase_date: Mapped[Date | None] = mapped_column(
        Date,
        nullable=True,
    )

    installation_date: Mapped[Date | None] = mapped_column(
        Date,
        nullable=True,
    )

    last_maintenance_date: Mapped[Date | None] = mapped_column(
        Date,
        nullable=True,
    )

    next_maintenance_date: Mapped[Date | None] = mapped_column(
        Date,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="Running",
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

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )