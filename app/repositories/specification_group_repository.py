"""
MKPrintingMasterPro ERP
Build-015

Specification Group Repository

Purpose:
Handles Dynamic Specification Group operations.

Status:
Production Ready
"""

from app.repositories.base_repository import BaseRepository
from app.models.specification_group import SpecificationGroup


class SpecificationGroupRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db, SpecificationGroup)

    # --------------------------------------------------
    # Get Groups By Template
    # --------------------------------------------------

    def get_by_template(self, template_id):

        return (
            self.db.query(SpecificationGroup)
            .filter(
                SpecificationGroup.template_id == template_id,
                SpecificationGroup.is_active == True,
            )
            .order_by(
                SpecificationGroup.display_order
            )
            .all()
        )

    # --------------------------------------------------
    # Get Group By Code
    # --------------------------------------------------

    def get_by_code(self, group_code):

        return (
            self.db.query(SpecificationGroup)
            .filter(
                SpecificationGroup.group_code == group_code
            )
            .first()
        )

    # --------------------------------------------------
    # Get Active Groups
    # --------------------------------------------------

    def get_active_groups(self):

        return (
            self.db.query(SpecificationGroup)
            .filter(
                SpecificationGroup.is_active == True
            )
            .order_by(
                SpecificationGroup.display_order
            )
            .all()
        )

    # --------------------------------------------------
    # Count Groups Under Template
    # --------------------------------------------------

    def count_by_template(self, template_id):

        return (
            self.db.query(SpecificationGroup)
            .filter(
                SpecificationGroup.template_id == template_id,
                SpecificationGroup.is_active == True,
            )
            .count()
        )