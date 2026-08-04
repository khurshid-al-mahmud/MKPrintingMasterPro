"""
MKPrintingMasterPro ERP

Product Template Model.

Purpose:
Master template definition for products.
Each Product can have one or more Templates.

Status:
Production Ready
"""

from datetime import datetime

from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.models.base import Base


class ProductTemplate(Base):
    """
    Product Template Master.
    """


    __tablename__ = "product_templates"


    # =====================================
    # Primary Key
    # =====================================

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )


    # =====================================
    # Template Information
    # =====================================

    template_code: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True,
    )


    template_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )


    product_id: Mapped[int] = mapped_column(
        ForeignKey(
            "products.id"
        ),
        nullable=False,
        index=True,
    )


    description: Mapped[str | None] = mapped_column(
        String(300),
        nullable=True,
    )


    # =====================================
    # Status
    # =====================================

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )


    # =====================================
    # Audit
    # =====================================

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False,
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


    # =====================================
    # Relationships
    # =====================================

    product = relationship(
        "Product",
        back_populates="templates",
    )


    # Specification Group
    specification_groups = relationship(
        "SpecificationGroup",
        back_populates="template",
        cascade="all, delete-orphan",
    )


    # Template Field Mapping
    template_fields = relationship(
        "TemplateFieldMapping",
        back_populates="template",
        cascade="all, delete-orphan",
    )


    # Specification Dependency Rule
    dependency_rules = relationship(
        "SpecificationDependencyRule",
        back_populates="template",
        cascade="all, delete-orphan",
    )


    # Formula Rule
    formula_rules = relationship(
        "FormulaRule",
        back_populates="template",
        cascade="all, delete-orphan",
    )


    # Template Version
    template_versions = relationship(
        "TemplateVersion",
        back_populates="template",
        cascade="all, delete-orphan",
    )


    # Specification Audit
    audit_logs = relationship(
        "SpecificationAudit",
        back_populates="template",
        cascade="all, delete-orphan",
    )


    def __repr__(self):

        return (
            f"<ProductTemplate("
            f"{self.template_code}, "
            f"{self.template_name})>"
        )