"""
Employee Profile Model.

Stores employee-specific information.

Every Employee Profile belongs to one Party.
"""

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)

from app.models.base import Base


class EmployeeProfile(Base):
    """Employee Profile."""

    __tablename__ = "employee_profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    party_id = Column(
        Integer,
        ForeignKey("parties.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    employee_number = Column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    department = Column(
        String(100),
        nullable=True,
    )

    designation = Column(
        String(100),
        nullable=True,
    )

    joining_date = Column(
        String(20),
        nullable=True,
    )

    employment_status = Column(
        String(50),
        nullable=True,
        default="Active",
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )