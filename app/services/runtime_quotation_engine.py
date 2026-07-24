"""
MKPrintingMasterPro ERP
Build-016B
Commit-01

Runtime Quotation Engine

Purpose:
Enterprise Runtime Coordinator

Status:
Compile Ready
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

        # Build-016 বর্তমানে এই দুইটি Engine db গ্রহণ করে না
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
        Build-016B Commit-01

        Skeleton Only

        Runtime Pipeline
        will be added in Commit-02.
        """

        return {

            "success": True,

            "build": "016B",

            "commit": "01",

            "template_id": template_id,

            "values": values,

        }