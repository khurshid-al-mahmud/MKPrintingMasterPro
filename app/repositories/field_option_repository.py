"""
MKPrintingMasterPro ERP
Build-015

Field Option Repository

Purpose:
Handles Dynamic Field Option operations.

Status:
Production Ready
"""

from app.repositories.base_repository import BaseRepository
from app.models.field_option import FieldOption


class FieldOptionRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db, FieldOption)

    # --------------------------------------------------
    # Get Options By Field
    # --------------------------------------------------

    def get_by_field(self, field_id):

        return (
            self.db.query(FieldOption)
            .filter(
                FieldOption.field_id == field_id,
                FieldOption.is_active == True,
            )
            .order_by(
                FieldOption.display_order
            )
            .all()
        )

    # --------------------------------------------------
    # Get Default Option
    # --------------------------------------------------

    def get_default_option(self, field_id):

        return (
            self.db.query(FieldOption)
            .filter(
                FieldOption.field_id == field_id,
                FieldOption.is_default == True,
                FieldOption.is_active == True,
            )
            .first()
        )

    # --------------------------------------------------
    # Get Option By Code
    # --------------------------------------------------

    def get_by_code(self, option_code):

        return (
            self.db.query(FieldOption)
            .filter(
                FieldOption.option_code == option_code
            )
            .first()
        )

    # --------------------------------------------------
    # Count Options
    # --------------------------------------------------

    def count_by_field(self, field_id):

        return (
            self.db.query(FieldOption)
            .filter(
                FieldOption.field_id == field_id,
                FieldOption.is_active == True,
            )
            .count()
        )