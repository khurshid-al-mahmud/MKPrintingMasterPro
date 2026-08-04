"""
MKPrintingMasterPro ERP
Build-013

Formula Rule Model

Purpose:
Stores Dynamic Formula Rules for
Quotation,
Costing,
Production,
Inventory,
AI.

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

from app.models.base import Base


class FormulaRule(Base):
    __tablename__ = "formula_rules"

    id = Column(Integer, primary_key=True, index=True)

    # -------------------------------------
    # Parent Template
    # -------------------------------------

    template_id = Column(
        Integer,
        ForeignKey("product_templates.id"),
        nullable=False
    )

    # -------------------------------------
    # Identity
    # -------------------------------------

    formula_code = Column(
        String(100),
        unique=True,
        nullable=False
    )

    formula_name_en = Column(
        String(200),
        nullable=False
    )

    formula_name_bn = Column(
        String(200),
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    # -------------------------------------
    # Formula
    # -------------------------------------

    formula_type = Column(
        String(100),
        nullable=False
    )
    # Example:
    # COST
    # QUOTATION
    # PAPER
    # PLATE
    # INK
    # MACHINE
    # BINDING
    # PACKAGING

    formula_expression = Column(
        Text,
        nullable=False
    )

    # -------------------------------------
    # Version
    # -------------------------------------

    version = Column(
        String(20),
        default="1.0"
    )

    effective_date = Column(
        DateTime,
        default=datetime.utcnow
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

    template = relationship(
        "ProductTemplate",
        back_populates="formula_rules"
    )

    def __repr__(self):

        return (
            f"<FormulaRule("
            f"{self.formula_code}, "
            f"{self.formula_name_en})>"
        )
