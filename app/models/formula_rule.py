"""
Formula Rule Model.

Stores all calculation formulas
used in Dynamic Specification Engine.
"""

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)

from sqlalchemy.orm import relationship

from app.models.base import Base


class FormulaRule(Base):
    """
    Formula Rule Master.
    """

    __tablename__ = "formula_rules"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    template_id = Column(
        Integer,
        ForeignKey("product_templates.id"),
        nullable=False,
    )

    formula_code = Column(
        String(100),
        unique=True,
        nullable=False,
    )

    formula_name_en = Column(
        String(200),
        nullable=False,
    )

    formula_name_bn = Column(
        String(200),
        nullable=True,
    )

    description = Column(
        Text,
        nullable=True,
    )

    formula_type = Column(
        String(100),
        nullable=False,
    )

    formula_expression = Column(
        Text,
        nullable=False,
    )

    version = Column(
        String(20),
        nullable=True,
    )

    effective_date = Column(
        DateTime,
        nullable=True,
    )

    is_default = Column(
        Boolean,
        default=False,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    created_by = Column(
        String(100),
        nullable=True,
    )

    updated_by = Column(
        String(100),
        nullable=True,
    )

    created_at = Column(
        DateTime,
        nullable=True,
    )

    updated_at = Column(
        DateTime,
        nullable=True,
    )

    template = relationship(
        "ProductTemplate",
        back_populates="formula_rules",
    )