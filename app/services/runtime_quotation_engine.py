"""
MKPrintingMasterPro ERP
Build-015B

Runtime Quotation Engine V2

Purpose:
Runs Complete Dynamic Runtime Pipeline.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.services.dynamic_specification_service import (
    DynamicSpecificationService,
)
from app.services.validation_engine import (
    ValidationEngine,
)
from app.services.dependency_engine import (
    DependencyEngine,
)
from app.services.formula_engine import (
    FormulaEngine,
)


class RuntimeQuotationEngine:

    def __init__(self, db: Session):

        self.db = db

        self.spec_service = DynamicSpecificationService(db)
        self.validation_engine = ValidationEngine()
        self.dependency_engine = DependencyEngine(db)
        self.formula_engine = FormulaEngine(db)

    # --------------------------------------------------

    def run(
        self,
        template_id: int,
        values: dict,
    ):

        runtime = self.spec_service.load_template(
            template_id
        )

        if runtime is None:

            return {
                "success": False,
                "message": "Template Not Found"
            }

        validation_errors = []

        # ----------------------------
        # Validation
        # ----------------------------

        for group_data in runtime["groups"]:

            for field_data in group_data["fields"]:

                field = field_data["field"]

                value = values.get(field.id)

                valid, message = (
                    self.validation_engine.validate(
                        value,
                        field,
                    )
                )

                if not valid:

                    validation_errors.append(

                        {
                            "field_id": field.id,
                            "field_name": field.field_name_en,
                            "message": message,
                        }

                    )

        # ----------------------------
        # Dependency
        # ----------------------------

        dependency_result = (
            self.dependency_engine.evaluate(
                template_id,
                values,
            )
        )

        # ----------------------------
        # Formula
        # ----------------------------

        formula_result = (
            self.formula_engine.calculate_all(
                template_id,
                values,
            )
        )

        return {

            "success": len(validation_errors) == 0,

            "template": runtime["template"],

            "groups": runtime["groups"],

            "validation_errors": validation_errors,

            "dependency": dependency_result,

            "formula": formula_result,

        }