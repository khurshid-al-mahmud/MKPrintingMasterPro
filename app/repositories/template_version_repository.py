"""
MKPrintingMasterPro ERP
Build-015A

Template Version Repository

Purpose:
Repository for TemplateVersion CRUD operations.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.models.template_version import TemplateVersion
from app.repositories.base_repository import BaseRepository


class TemplateVersionRepository(BaseRepository):
    """
    Template Version Repository
    """

    def __init__(self, db: Session):
        super().__init__(db, TemplateVersion)

    # ------------------------------------------
    # Find by ID
    # ------------------------------------------

    def get_by_id(self, version_id: int):
        return (
            self.db.query(TemplateVersion)
            .filter(
                TemplateVersion.id == version_id
            )
            .first()
        )

    # ------------------------------------------
    # Current Version
    # ------------------------------------------

    def get_current_version(self, template_id: int):
        return (
            self.db.query(TemplateVersion)
            .filter(
                TemplateVersion.template_id == template_id,
                TemplateVersion.is_current.is_(True)
            )
            .first()
        )

    # ------------------------------------------
    # Version History
    # ------------------------------------------

    def get_version_history(self, template_id: int):
        return (
            self.db.query(TemplateVersion)
            .filter(
                TemplateVersion.template_id == template_id
            )
            .order_by(
                TemplateVersion.version_number.desc()
            )
            .all()
        )

    # ------------------------------------------
    # Create
    # ------------------------------------------

    def create_version(
        self,
        version: TemplateVersion,
    ):
        self.db.add(version)
        self.db.commit()
        self.db.refresh(version)
        return version

    # ------------------------------------------
    # Update
    # ------------------------------------------

    def update_version(self):
        self.db.commit()

    # ------------------------------------------
    # Delete
    # ------------------------------------------

    def delete_version(
        self,
        version: TemplateVersion,
    ):
        self.db.delete(version)
        self.db.commit()