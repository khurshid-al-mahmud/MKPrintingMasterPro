"""
MKPrintingMasterPro ERP
Build-013

Validation Rule Model

Purpose:
Stores Dynamic Validation Rules
for Specification Fields.

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


class ValidationRule(Base):
    __tablename__ = "validation_rules"

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
    # Rule Identity
    # -------------------------------------

    rule_code = Column(
        String(100),
        unique=True,
        nullable=False
    )

    rule_name = Column(
        String(200),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    # -------------------------------------
    # Validation Type
    # -------------------------------------

    validation_type = Column(
        String(100),
        nullable=False
    )

    # Examples:
    # REQUIRED
    # MIN
    # MAX
    # RANGE
    # REGEX
    # EMAIL
    # PHONE
    # DATE
    # UNIQUE
    # CUSTOM

    # -------------------------------------
    # Validation Values
    # -------------------------------------

    minimum_value = Column(String(100))

    maximum_value = Column(String(100))

    regex_pattern = Column(Text)

    validation_expression = Column(Text)

    error_message = Column(Text)

    # -------------------------------------
    # Behaviour
    # -------------------------------------

    stop_processing = Column(
        Boolean,
        default=True
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
    back_populates="validation_rules"
)

def __repr__(self):

        return (
            f"<ValidationRule("
            f"{self.rule_code})>"
        )