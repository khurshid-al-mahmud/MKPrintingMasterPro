"""
Customer Profile Model.

Stores customer-specific information.

Every Customer Profile belongs to one Party.
"""

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    Numeric,
    String,
)

from app.models.base import Base


class CustomerProfile(Base):
    """Customer Profile."""

    __tablename__ = "customer_profiles"

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

    customer_number = Column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    customer_category = Column(
        String(100),
        nullable=True,
    )

    credit_limit = Column(
        Numeric(12, 2),
        nullable=False,
        default=0,
    )

    credit_days = Column(
        Integer,
        nullable=False,
        default=0,
    )

    price_category = Column(
        String(100),
        nullable=True,
    )

    discount_rate = Column(
        Numeric(5, 2),
        nullable=False,
        default=0,
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )