"""
MKPrintingMasterPro ERP
Build-013

Specification Audit Model

Purpose:
Maintains complete audit history of Dynamic
Specification changes.

Status:
Production Ready
"""

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Text
)

from sqlalchemy.orm import relationship

from app.models.base import Base


class SpecificationAudit(Base):
    __tablename__ = "specification_audits"

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
    # Change Information
    # -------------------------------------

    action = Column(
        String(50),
        nullable=False
    )
    # CREATE
    # UPDATE
    # DELETE
    # ENABLE
    # DISABLE
    # REORDER

    table_name = Column(
        String(100),
        nullable=False
    )

    record_id = Column(
        Integer,
        nullable=False
    )

    field_name = Column(
        String(100),
        nullable=True
    )

    old_value = Column(
        Text,
        nullable=True
    )

    new_value = Column(
        Text,
        nullable=True
    )

    change_reason = Column(
        Text,
        nullable=True
    )

    # -------------------------------------
    # User
    # -------------------------------------

    changed_by = Column(
        String(100),
        nullable=False
    )

    user_role = Column(
        String(100),
        nullable=True
    )

    # -------------------------------------
    # Timestamp
    # -------------------------------------

    changed_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # -------------------------------------
    # Relationship
    # -------------------------------------

    template = relationship(
        "ProductTemplate",
        back_populates="audit_logs"
    )

    def __repr__(self):

        return (
            f"<SpecificationAudit("
            f"{self.action}, "
            f"{self.changed_by})>"
        )
