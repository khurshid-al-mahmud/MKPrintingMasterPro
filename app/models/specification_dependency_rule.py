"""
MKPrintingMasterPro ERP
Build-013

Specification Dependency Rule Model

Purpose:
Controls Dynamic Field Visibility and Dependency Rules.

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


class SpecificationDependencyRule(Base):
    __tablename__ = "specification_dependency_rules"

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
    # Source Field
    # -------------------------------------

    source_field_id = Column(
        Integer,
        ForeignKey("specification_fields.id"),
        nullable=False
    )

    # -------------------------------------
    # Trigger Value
    # -------------------------------------

    trigger_value = Column(
        String(255),
        nullable=False
    )

    # -------------------------------------
    # Target Field
    # -------------------------------------

    target_field_id = Column(
        Integer,
        ForeignKey("specification_fields.id"),
        nullable=False
    )

    # -------------------------------------
    # Action
    # -------------------------------------

    action = Column(
        String(50),
        nullable=False
    )
    # Example:
    # SHOW
    # HIDE
    # REQUIRE
    # OPTIONAL
    # READONLY
    # ENABLE
    # DISABLE

    # -------------------------------------
    # Rule Description
    # -------------------------------------

    description = Column(
        Text,
        nullable=True
    )

    priority = Column(
        Integer,
        default=1
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
    # Relationships
    # -------------------------------------

    template = relationship(
        "ProductTemplate",
        back_populates="dependency_rules"
    )

    source_field = relationship(
    "SpecificationField",
    foreign_keys=[source_field_id],
    back_populates="dependency_rules",
)
    
    target_field = relationship(
        "SpecificationField",
        foreign_keys=[target_field_id]
    )

    def __repr__(self):
        return (
            f"<DependencyRule("
            f"Source={self.source_field_id}, "
            f"Target={self.target_field_id}, "
            f"Action={self.action})>"
        )
