"""
MKPrintingMasterPro ERP
Build-015

Product Template Repository

Purpose:
Handles Product Template database operations.

Status:
Production Ready
"""

from app.repositories.base_repository import BaseRepository
from app.models.product_template import ProductTemplate


class ProductTemplateRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db, ProductTemplate)

    # --------------------------------------------------
    # Get Active Template
    # --------------------------------------------------

    def get_active_template(
        self,
        product_category_id,
        construction_type_id=None,
    ):

        query = (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.product_category_id == product_category_id,
                ProductTemplate.is_active == True,
            )
        )

        if construction_type_id is not None:

            query = query.filter(
                ProductTemplate.construction_type_id == construction_type_id
            )

        return query.first()

    # --------------------------------------------------
    # Get Default Template
    # --------------------------------------------------

    def get_default_template(self):

        return (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.is_default == True,
                ProductTemplate.is_active == True,
            )
            .first()
        )

    # --------------------------------------------------
    # Get By Template Code
    # --------------------------------------------------

    def get_by_code(self, template_code):

        return (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.template_code == template_code
            )
            .first()
        )

    # --------------------------------------------------
    # Get All Active Templates
    # --------------------------------------------------

    def get_active_templates(self):

        return (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.is_active == True
            )
            .order_by(
                ProductTemplate.template_name_en
            )
            .all()
        )