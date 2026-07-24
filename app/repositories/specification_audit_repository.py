"""
MKPrintingMasterPro ERP
Build-015A

Specification Audit Repository

Purpose:
Repository for SpecificationAudit CRUD operations.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.models.specification_audit import SpecificationAudit
from app.repositories.base_repository import BaseRepository


class SpecificationAuditRepository(BaseRepository):
    """
    Specification Audit Repository
    """

    def __init__(self, db: Session):
        super().__init__(db, SpecificationAudit)

    # ------------------------------------------
    # Find by ID
    # ------------------------------------------

    def get_by_id(self, audit_id: int):
        return (
            self.db.query(SpecificationAudit)
            .filter(
                SpecificationAudit.id == audit_id
            )
            .first()
        )

    # ------------------------------------------
    # Audit By Template
    # ------------------------------------------

    def get_by_template(self, template_id: int):
        return (
            self.db.query(SpecificationAudit)
            .filter(
                SpecificationAudit.template_id == template_id
            )
            .order_by(
                SpecificationAudit.changed_at.desc()
            )
            .all()
        )

    # ------------------------------------------
    # Audit By User
    # ------------------------------------------

    def get_by_user(self, username: str):
        return (
            self.db.query(SpecificationAudit)
            .filter(
                SpecificationAudit.changed_by == username
            )
            .order_by(
                SpecificationAudit.changed_at.desc()
            )
            .all()
        )

    # ------------------------------------------
    # Create
    # ------------------------------------------

    def create_log(
        self,
        audit: SpecificationAudit,
    ):
        self.db.add(audit)
        self.db.commit()
        self.db.refresh(audit)
        return audit

    # ------------------------------------------
    # Delete
    # ------------------------------------------

    def delete_log(
        self,
        audit: SpecificationAudit,
    ):
        self.db.delete(audit)
        self.db.commit()