"""
MKPrintingMasterPro ERP
Build-016

Pricing Engine

Purpose:
Converts Production Cost
into Customer Selling Price.

Status:
Production Ready
"""

from decimal import Decimal
from typing import Dict


class PricingEngine:

    def __init__(self):

        self.total_cost = Decimal("0")

        self.profit_percent = Decimal("0")

        self.vat_percent = Decimal("0")

        self.discount_percent = Decimal("0")

    # --------------------------------------------------
    # Set Base Cost
    # --------------------------------------------------

    def set_cost(
        self,
        cost: Decimal,
    ):

        self.total_cost = Decimal(cost)

    # --------------------------------------------------
    # Profit
    # --------------------------------------------------

    def set_profit_percent(
        self,
        percent: Decimal,
    ):

        self.profit_percent = Decimal(percent)

    # --------------------------------------------------
    # VAT
    # --------------------------------------------------

    def set_vat_percent(
        self,
        percent: Decimal,
    ):

        self.vat_percent = Decimal(percent)

    # --------------------------------------------------
    # Discount
    # --------------------------------------------------

    def set_discount_percent(
        self,
        percent: Decimal,
    ):

        self.discount_percent = Decimal(percent)

    # --------------------------------------------------
    # Profit Amount
    # --------------------------------------------------

    def profit_amount(self) -> Decimal:

        return (
            self.total_cost
            * self.profit_percent
            / Decimal("100")
        )

    # --------------------------------------------------
    # Selling Price
    # --------------------------------------------------

    def selling_price(self) -> Decimal:

        return (
            self.total_cost
            + self.profit_amount()
        )

    # --------------------------------------------------
    # VAT Amount
    # --------------------------------------------------

    def vat_amount(self) -> Decimal:

        return (
            self.selling_price()
            * self.vat_percent
            / Decimal("100")
        )

    # --------------------------------------------------
    # Discount Amount
    # --------------------------------------------------

    def discount_amount(self) -> Decimal:

        return (
            self.selling_price()
            * self.discount_percent
            / Decimal("100")
        )

    # --------------------------------------------------
    # Final Customer Price
    # --------------------------------------------------

    def final_price(self) -> Decimal:

        return (

            self.selling_price()

            + self.vat_amount()

            - self.discount_amount()

        )

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    def export(self) -> Dict:

        return {

            "cost": self.total_cost,

            "profit_percent": self.profit_percent,

            "profit_amount": self.profit_amount(),

            "selling_price": self.selling_price(),

            "vat_percent": self.vat_percent,

            "vat_amount": self.vat_amount(),

            "discount_percent": self.discount_percent,

            "discount_amount": self.discount_amount(),

            "final_price": self.final_price(),

        }

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        self.total_cost = Decimal("0")

        self.profit_percent = Decimal("0")

        self.vat_percent = Decimal("0")

        self.discount_percent = Decimal("0")