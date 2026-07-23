"""
MKPrintingMasterPro ERP
Build-013

Field Option Model

Purpose:
Stores Dynamic Dropdown / ComboBox / Radio Options.

Status:
Production Ready
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship

from app.database.base import Base


class FieldOption(Base):
    __tablename__ = "field_options"

    id = Column(Integer, primary_key=True, index=True)

    # -------------------------------------
    # Parent Field
    # -------------------------------------

    field_id = Column(
        Integer,
        ForeignKey("specification_fields.id"),
        nullable=False
    )

    # -------------------------------------
    # Identity
    # -------------------------------------

    option_code = Column(
        String(100),
        nullable=False
    )

    option_name_en = Column(
        String(200),
        nullable=False
    )

    option_name_bn = Column(
        String(200),
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    # -------------------------------------
    # Value
    # -------------------------------------

    option_value = Column(
        String(200),
        nullable=False
    )

    display_order = Column(
        Integer,
        default=1
    )

    # -------------------------------------
    # Behaviour
    # -------------------------------------

    is_default = Column(
        Boolean,
        default=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    # -------------------------------------
    # Audit
    # -------------------------------------

    created_by = Column(String(100))

    updated_by = Column(String(100))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # -------------------------------------
    # Relationship
    # -------------------------------------

    field = relationship(
        "SpecificationField",
        back_populates="field_options"
    )

    def __repr__(self):

        return (
            f"<FieldOption("
            f"{self.option_name_en})>"
        )