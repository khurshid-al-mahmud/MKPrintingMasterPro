"""
MKPrintingMasterPro ERP
Build-015

Specification Field Repository

Purpose:
Handles Dynamic Specification Field operations.

Status:
Production Ready
"""

from app.repositories.base_repository import BaseRepository
from app.models.specification_field import SpecificationField


class SpecificationFieldRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db, SpecificationField)

    # --------------------------------------------------
    # Get Fields By Group
    # --------------------------------------------------

    def get_by_group(self, group_id):

        return (
            self.db.query(SpecificationField)
            .filter(
                SpecificationField.group_id == group_id,
                SpecificationField.is_active == True,
                SpecificationField.is_visible == True,
            )
            .order_by(
                SpecificationField.display_order
            )
            .all()
        )

    # --------------------------------------------------
    # Get Field By Code
    # --------------------------------------------------

    def get_by_code(self, field_code):

        return (
            self.db.query(SpecificationField)
            .filter(
                SpecificationField.field_code == field_code
            )
            .first()
        )

    # --------------------------------------------------
    # Get Required Fields
    # --------------------------------------------------

    def get_required_fields(self, group_id):

        return (
            self.db.query(SpecificationField)
            .filter(
                SpecificationField.group_id == group_id,
                SpecificationField.is_required == True,
                SpecificationField.is_active == True,
            )
            .order_by(
                SpecificationField.display_order
            )
            .all()
        )

    # --------------------------------------------------
    # Get Calculated Fields
    # --------------------------------------------------

    def get_calculated_fields(self, group_id):

        return (
            self.db.query(SpecificationField)
            .filter(
                SpecificationField.group_id == group_id,
                SpecificationField.is_calculated == True,
                SpecificationField.is_active == True,
            )
            .order_by(
                SpecificationField.display_order
            )
            .all()
        )

    # --------------------------------------------------
    # Count Fields
    # --------------------------------------------------

    def count_by_group(self, group_id):

        return (
            self.db.query(SpecificationField)
            .filter(
                SpecificationField.group_id == group_id,
                SpecificationField.is_active == True,
            )
            .count()
        )