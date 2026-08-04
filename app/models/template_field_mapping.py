"""
MKPrintingMasterPro ERP
Build-013

Template Field Mapping Model

Purpose:
Maps Specification Fields to Product Templates.

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


class TemplateFieldMapping(Base):
    __tablename__ = "template_field_mapping"

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
    # Specification Field
    # -------------------------------------

    field_id = Column(
        Integer,
        ForeignKey("specification_fields.id"),
        nullable=False
    )

    # -------------------------------------
    # Behaviour
    # -------------------------------------

    is_required = Column(
        Boolean,
        default=False
    )

    is_optional = Column(
        Boolean,
        default=True
    )

    is_visible = Column(
        Boolean,
        default=True
    )

    is_editable = Column(
        Boolean,
        default=True
    )

    is_readonly = Column(
        Boolean,
        default=False
    )

    # -------------------------------------
    # Default Value
    # -------------------------------------

    default_value = Column(
        String(255),
        nullable=True
    )

    # -------------------------------------
    # Display
    # -------------------------------------

    display_order = Column(
        Integer,
        default=1
    )

    group_order = Column(
        Integer,
        default=1
    )

    column_width = Column(
        Integer,
        default=12
    )

    # -------------------------------------
    # UI Behaviour
    # -------------------------------------

    show_in_quotation = Column(
        Boolean,
        default=True
    )

    show_in_job_order = Column(
        Boolean,
        default=True
    )

    show_in_production = Column(
        Boolean,
        default=True
    )

    show_in_invoice = Column(
        Boolean,
        default=False
    )

    # -------------------------------------
    # Validation Override
    # -------------------------------------

    validation_override = Column(
        Text,
        nullable=True
    )

    # -------------------------------------
    # Formula Override
    # -------------------------------------

    formula_override = Column(
        Text,
        nullable=True
    )

    # -------------------------------------
    # Status
    # -------------------------------------

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
        back_populates="template_fields"
    )

    field = relationship(
        "SpecificationField",
        back_populates="template_mappings"
    )

    def __repr__(self):

        return (
            f"<TemplateFieldMapping("
            f"Template={self.template_id}, "
            f"Field={self.field_id})>"
        )
