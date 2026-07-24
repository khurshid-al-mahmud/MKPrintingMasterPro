"""
MKPrintingMasterPro ERP
Build-015B

Dynamic Specification Service

Purpose:
Loads complete Dynamic Specification Template
using Template ID.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.repositories.product_template_repository import (
    ProductTemplateRepository,
)

from app.repositories.specification_group_repository import (
    SpecificationGroupRepository,
)

from app.repositories.specification_field_repository import (
    SpecificationFieldRepository,
)

from app.repositories.field_option_repository import (
    FieldOptionRepository,
)


class DynamicSpecificationService:

    def __init__(self, db: Session):

        self.db = db

        self.template_repo = ProductTemplateRepository(db)

        self.group_repo = SpecificationGroupRepository(db)

        self.field_repo = SpecificationFieldRepository(db)

        self.option_repo = FieldOptionRepository(db)

    # --------------------------------------------------
    # Load Complete Template
    # --------------------------------------------------

    def load_template(
        self,
        template_id: int,
    ):

        # -----------------------------
        # Template
        # -----------------------------

        template = self.template_repo.get_by_id(
            template_id
        )

        if template is None:

            return None

        # -----------------------------
        # Groups
        # -----------------------------

        groups = self.group_repo.get_by_template(
            template.id
        )

        result = {

            "template": template,

            "groups": []

        }

        # -----------------------------
        # Group Loop
        # -----------------------------

        for group in groups:

            fields = self.field_repo.get_by_group(
                group.id
            )

            group_data = {

                "group": group,

                "fields": []

            }

            # -------------------------
            # Field Loop
            # -------------------------

            for field in fields:

                options = self.option_repo.get_by_field(
                    field.id
                )

                field_data = {

                    "field": field,

                    "options": options

                }

                group_data["fields"].append(
                    field_data
                )

            result["groups"].append(
                group_data
            )

        return result