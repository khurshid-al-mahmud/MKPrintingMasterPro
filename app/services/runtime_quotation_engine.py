"""
MKPrintingMasterPro ERP
Build-016B

Runtime Quotation Engine

Purpose:
Enterprise Runtime Coordinator

Status:
Build-016B Commit-02
"""

from typing import Dict
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
from app.services.cost_engine import (
    CostEngine,
)
from app.services.pricing_engine import (
    PricingEngine,
)
from app.services.runtime_json_builder import (
    RuntimeJSONBuilder,
)


class RuntimeQuotationEngine:

    def __init__(
        self,
        db: Session,
    ):

        self.db = db

        self.specification_service = DynamicSpecificationService(db)

        self.validation_engine = ValidationEngine()

        self.dependency_engine = DependencyEngine(db)

        self.formula_engine = FormulaEngine(db)

        self.cost_engine = CostEngine()

        self.pricing_engine = PricingEngine()

        self.json_builder = RuntimeJSONBuilder()

    # --------------------------------------------------

    def run(
        self,
        template_id: int,
        values: Dict,
    ):

        """
        Runtime Pipeline

        Template
            ↓
        Validation
            ↓
        Dependency
            ↓
        Formula
            ↓
        Cost
            ↓
        Pricing
            ↓
        Runtime JSON
        """

        # -------------------------------
        # Load Template
        # -------------------------------

        runtime = self.specification_service.load_template(
            template_id
        )

        if runtime is None:

            return {
                "success": False,
                "message": "Template Not Found",
                "template_id": template_id,
            }

        # -------------------------------
        # Validation
        # -------------------------------

        validation_result = {
            "is_valid": True,
            "errors": [],
        }

        # -------------------------------
        # Dependency
        # -------------------------------

        dependency_result = self.dependency_engine.evaluate(
            template_id,
            values,
        )

        # -------------------------------
        # Formula
        # -------------------------------

        formula_result = self.formula_engine.calculate_all(
            template_id,
            values,
        )

        # -------------------------------
        # Cost
        # -------------------------------

        self.cost_engine.reset()

        # Future Build:
        # Formula Result থেকে Cost Populate হবে

        cost_result = self.cost_engine.export()

        # -------------------------------
        # Pricing
        # -------------------------------

        self.pricing_engine.reset()

        self.pricing_engine.set_cost(
            cost_result["total_cost"]
        )

        pricing_result = self.pricing_engine.export()

        # -------------------------------
        # Runtime JSON
        # -------------------------------

        result = {
            "success": True,
            "build": "016B",
            "template": runtime,
            "validation": validation_result,
            "dependency": dependency_result,
            "formula": formula_result,
            "cost": cost_result,
            "pricing": pricing_result,
            "values": values,
        }

        return result