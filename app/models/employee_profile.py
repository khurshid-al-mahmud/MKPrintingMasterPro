"""
Employee Profile Model.

Stores employee-specific information.

Every Employee Profile belongs to one Party.
"""

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class EmployeeProfile(Base):
    """Employee Profile."""

    __tablename__ = "employee_profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True,
    )

    party_id: Mapped[int] = mapped_column(
        ForeignKey("parties.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    employee_number: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    department: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    designation: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    joining_date: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    employment_status: Mapped[str] = mapped_column(
        String(50),
        default="Active",
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )