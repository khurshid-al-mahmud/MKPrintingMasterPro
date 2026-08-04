# ===== START SpecificationField.py PART-1 =====

"""
MKPrintingMasterPro ERP
Build-013

Specification Field Model

Purpose:
Stores every Dynamic Specification Field.

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
    Text,
)

from sqlalchemy.orm import relationship

from app.models.base import Base

from app.models.specification_group import SpecificationGroup
from app.models.field_option import FieldOption


class SpecificationField(Base):

    __tablename__ = "specification_fields"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Identity

    field_code = Column(
        String(100),
        unique=True,
        nullable=False
    )

    field_name_en = Column(
        String(200),
        nullable=False
    )

    field_name_bn = Column(
        String(200),
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    # Parent Group

    group_id = Column(
        Integer,
        ForeignKey("specification_groups.id"),
        nullable=False
    )

    # Data Type

    data_type = Column(
        String(50),
        nullable=False
    )

    input_control = Column(
        String(50),
        nullable=False
    )

    # UI

    placeholder_en = Column(String(200))

    placeholder_bn = Column(String(200))

    default_value = Column(String(200))

    help_text = Column(Text)

    icon = Column(String(100))


    # Behaviour

    is_required = Column(
        Boolean,
        default=False
    )

    is_editable = Column(
        Boolean,
        default=True
    )

    is_visible = Column(
        Boolean,
        default=True
    )

    is_calculated = Column(
        Boolean,
        default=False
    )

    is_system_field = Column(
        Boolean,
        default=False
    )


    # Display

    display_order = Column(
        Integer,
        default=1
    )

    width = Column(
        Integer,
        default=12
    )


    # Validation

    minimum_value = Column(
        String(100)
    )

    maximum_value = Column(
        String(100)
    )

    minimum_length = Column(
        Integer
    )

    maximum_length = Column(
        Integer
    )

    regex_pattern = Column(
        Text
    )

    validation_message = Column(
        Text
    )


    # Unit

    unit = Column(
        String(100)
    )


    # Formula

    formula_reference = Column(
        String(200)
    )


    # Status

    is_active = Column(
        Boolean,
        default=True
    )


    # Audit

    created_by = Column(
        String(100)
    )

    updated_by = Column(
        String(100)
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    # Relationship

    group = relationship(
        "SpecificationGroup",
        back_populates="fields"
    )


    field_options = relationship(
        "FieldOption",
        back_populates="field",
        cascade="all, delete-orphan"
    )


    template_mappings = relationship(
        "TemplateFieldMapping",
        back_populates="field",
        cascade="all, delete-orphan"
    )


    validation_rules = relationship(
        "ValidationRule",
        back_populates="field",
        cascade="all, delete-orphan"
    )


    # Dependency Rules (Source Field)

    dependency_rules = relationship(
        "SpecificationDependencyRule",
        foreign_keys="SpecificationDependencyRule.source_field_id",
        back_populates="source_field",
        cascade="all, delete-orphan",
    )


    # Dependency Rules (Target Field)

    target_dependency_rules = relationship(
        "SpecificationDependencyRule",
        foreign_keys="SpecificationDependencyRule.target_field_id",
        back_populates="target_field",
        cascade="all, delete-orphan",
    )


    def __repr__(self):

        return (
            f"<SpecificationField("
            f"{self.field_code}, "
            f"{self.field_name_en})>"
        )