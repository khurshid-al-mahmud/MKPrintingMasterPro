"""
MKPrintingMasterPro ERP
Build-013
Product Template Model

Purpose:
Stores Dynamic Product Specification Templates.

Example:
Book + Paperback
Book + Hard Cover
Magazine + Center Pin
Medicine Box
Visiting Card

Status:
Production Ready
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database.base import Base

from datetime import datetime


class ProductTemplate(Base):
    __tablename__ = "product_templates"

    id = Column(Integer, primary_key=True, index=True)

    # ------------------------------
    # Identity
    # ------------------------------

    template_code = Column(String(50), unique=True, nullable=False)

    template_name_en = Column(String(200), nullable=False)

    template_name_bn = Column(String(200), nullable=True)

    description = Column(Text, nullable=True)

    # ------------------------------
    # Relations
    # ------------------------------

    product_category_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    construction_type_id = Column(
        Integer,
        ForeignKey("binding_types.id"),
        nullable=True
    )

    # ------------------------------
    # Language Support
    # ------------------------------

    enable_bangla = Column(Boolean, default=True)

    enable_english = Column(Boolean, default=True)

    # ------------------------------
    # Status
    # ------------------------------

    is_active = Column(Boolean, default=True)

    is_default = Column(Boolean, default=False)

    version = Column(String(20), default="1.0")

    # ------------------------------
    # Audit
    # ------------------------------

    created_by = Column(String(100), nullable=True)

    updated_by = Column(String(100), nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # ------------------------------
    # Relationships
    # ------------------------------

    product = relationship("Product")

    construction = relationship("BindingType")

    specification_groups = relationship(
        "SpecificationGroup",
        back_populates="template",
        cascade="all, delete-orphan"
    )

    template_fields = relationship(
        "TemplateFieldMapping",
        back_populates="template",
        cascade="all, delete-orphan"
    )

    dependency_rules = relationship(
        "SpecificationDependencyRule",
        back_populates="template",
        cascade="all, delete-orphan"
    )

    formula_rules = relationship(
        "FormulaRule",
        back_populates="template",
        cascade="all, delete-orphan"
    )

    audit_logs = relationship(
        "SpecificationAudit",
        back_populates="template",
        cascade="all, delete-orphan"
    )

    template_versions = relationship(
        "TemplateVersion",
        back_populates="template",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"<ProductTemplate("
            f"{self.template_code}, "
            f"{self.template_name_en})>"
        )