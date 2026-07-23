"""
MKPrintingMasterPro ERP
Build-013

Specification Group Model

Purpose:
Stores Dynamic Specification Groups.

Example

General
Paper
Printing
Binding
Finishing
Packaging
Machine
Cost

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


class SpecificationGroup(Base):
    __tablename__ = "specification_groups"

    id = Column(Integer, primary_key=True, index=True)

    # -------------------------
    # Identity
    # -------------------------

    group_code = Column(
        String(50),
        unique=True,
        nullable=False
    )

    group_name_en = Column(
        String(150),
        nullable=False
    )

    group_name_bn = Column(
        String(150),
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    # -------------------------
    # Parent Template
    # -------------------------

    template_id = Column(
        Integer,
        ForeignKey("product_templates.id"),
        nullable=False
    )

    # -------------------------
    # Display
    # -------------------------

    display_order = Column(
        Integer,
        default=1
    )

    icon = Column(
        String(100),
        nullable=True
    )

    collapsible = Column(
        Boolean,
        default=False
    )

    collapsed_default = Column(
        Boolean,
        default=False
    )

    # -------------------------
    # Status
    # -------------------------

    is_active = Column(
        Boolean,
        default=True
    )

    # -------------------------
    # Audit
    # -------------------------

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

    # -------------------------
    # Relationship
    # -------------------------

    template = relationship(
        "ProductTemplate",
        back_populates="specification_groups"
    )

    fields = relationship(
        "SpecificationField",
        back_populates="group",
        cascade="all, delete-orphan"
    )

    def __repr__(self):

        return (
            f"<SpecificationGroup("
            f"{self.group_code}, "
            f"{self.group_name_en})>"
        )