"""
MKPrintingMasterPro ERP
Build-013

Template Version Model

Purpose:
Maintains complete version history of every
Dynamic Product Specification Template.

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


class TemplateVersion(Base):
    __tablename__ = "template_versions"

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
    # Version Information
    # -------------------------------------

    version_number = Column(
        String(20),
        nullable=False
    )

    version_name = Column(
        String(100),
        nullable=True
    )

    description = Column(
        Text,
        nullable=True
    )

    # -------------------------------------
    # Status
    # -------------------------------------

    is_current = Column(
        Boolean,
        default=False
    )

    is_active = Column(
        Boolean,
        default=True
    )

    # -------------------------------------
    # Effective Date
    # -------------------------------------

    effective_from = Column(
        DateTime,
        default=datetime.utcnow
    )

    effective_to = Column(
        DateTime,
        nullable=True
    )

    # -------------------------------------
    # Audit
    # -------------------------------------

    created_by = Column(String(100))

    approved_by = Column(String(100))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    approved_at = Column(
        DateTime,
        nullable=True
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    # -------------------------------------
    # Relationship
    # -------------------------------------

    template = relationship("ProductTemplate")

    def __repr__(self):

        return (
            f"<TemplateVersion("
            f"{self.version_number})>"
        )