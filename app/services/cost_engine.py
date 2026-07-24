"""
MKPrintingMasterPro ERP
Build-016

Cost Engine

Purpose:
Calculates Total Production Cost
for any Printing Product.

Status:
Production Ready
"""

from decimal import Decimal
from typing import Dict


class CostEngine:

    def __init__(self):

        self.cost = {
            "paper_cost": Decimal("0"),
            "ink_cost": Decimal("0"),
            "plate_cost": Decimal("0"),
            "machine_cost": Decimal("0"),
            "binding_cost": Decimal("0"),
            "finishing_cost": Decimal("0"),
            "labour_cost": Decimal("0"),
            "packing_cost": Decimal("0"),
            "delivery_cost": Decimal("0"),
            "other_cost": Decimal("0"),
        }

    # --------------------------------------------------
    # Set Individual Cost
    # --------------------------------------------------

    def set_cost(
        self,
        key: str,
        value: Decimal,
    ):

        if key not in self.cost:
            raise ValueError(
                f"Unknown Cost Type : {key}"
            )

        self.cost[key] = Decimal(value)

    # --------------------------------------------------
    # Get Individual Cost
    # --------------------------------------------------

    def get_cost(
        self,
        key: str,
    ) -> Decimal:

        return self.cost.get(
            key,
            Decimal("0"),
        )

    # --------------------------------------------------
    # Total Production Cost
    # --------------------------------------------------

    def total_cost(self) -> Decimal:

        total = Decimal("0")

        for value in self.cost.values():

            total += value

        return total

    # --------------------------------------------------
    # Export Dictionary
    # --------------------------------------------------

    def export(self) -> Dict:

        return {

            **self.cost,

            "total_cost":

                self.total_cost()

        }

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        for key in self.cost:

            self.cost[key] = Decimal("0")