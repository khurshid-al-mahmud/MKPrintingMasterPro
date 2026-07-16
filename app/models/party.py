"""
Party Master Model.

This model stores all Individuals,
Businesses and Organizations.

Every Customer, Supplier,
Employee and Print Partner
starts as a Party.
"""

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
)

from sqlalchemy.sql import func

from app.models.base import Base


class Party(Base):
    """Party Master."""

    __tablename__ = "parties"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    party_type = Column(
        String(30),
        nullable=False,
    )

    party_name = Column(
        String(200),
        nullable=False,
        index=True,
    )

    display_name = Column(
        String(200),
        nullable=True,
    )

    mobile = Column(
        String(20),
        nullable=True,
        index=True,
    )

    alternate_mobile = Column(
        String(20),
        nullable=True,
    )

    whatsapp = Column(
        String(20),
        nullable=True,
    )

    email = Column(
        String(150),
        nullable=True,
    )

    website = Column(
        String(200),
        nullable=True,
    )

    address = Column(
        Text,
        nullable=True,
    )

    area = Column(
        String(100),
        nullable=True,
    )

    district = Column(
        String(100),
        nullable=True,
    )

    division = Column(
        String(100),
        nullable=True,
    )

    country = Column(
        String(100),
        nullable=True,
        default="Bangladesh",
    )

    remarks = Column(
        Text,
        nullable=True,
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )