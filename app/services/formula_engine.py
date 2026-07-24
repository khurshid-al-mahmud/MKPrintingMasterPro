"""
MKPrintingMasterPro ERP
Build-015B

Formula Engine

Purpose:
Executes Dynamic Formula Rules
stored inside Database.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.repositories.formula_rule_repository import (
    FormulaRuleRepository,
)


class FormulaEngine:

    def __init__(self, db: Session):

        self.db = db

        self.repository = FormulaRuleRepository(db)

    # --------------------------------------------------
    # Get Formula Rules
    # --------------------------------------------------

    def get_rules(
        self,
        template_id: int,
    ):

        return self.repository.get_by_template(
            template_id
        )

    # --------------------------------------------------
    # Execute Formula
    # --------------------------------------------------

    def execute_formula(
        self,
        expression,
        values: dict,
    ):

        try:

            safe_globals = {

                "__builtins__": {},

                "min": min,

                "max": max,

                "round": round,

                "abs": abs,

                "int": int,

                "float": float,

                "sum": sum,

            }

            return eval(
                str(expression),
                safe_globals,
                values,
            )

        except Exception:

            return None

    # --------------------------------------------------
    # Calculate One Rule
    # --------------------------------------------------

    def calculate_single(
        self,
        formula_rule,
        values: dict,
    ):

        return self.execute_formula(
            formula_rule.formula_expression,
            values,
        )

    # --------------------------------------------------
    # Calculate All Rules
    # --------------------------------------------------

    def calculate(
        self,
        template_id: int,
        values: dict,
    ):

        rules = self.get_rules(
            template_id
        )

        result = {}

        for rule in rules:

            output = self.execute_formula(
                rule.formula_expression,
                values,
            )

            result[
                str(rule.formula_code)
            ] = output

        return result

    # --------------------------------------------------
    # Sequential Calculation
    # --------------------------------------------------

    def calculate_all(
        self,
        template_id: int,
        values: dict,
    ):

        calculated = values.copy()

        rules = self.get_rules(
            template_id
        )

        for rule in rules:

            output = self.execute_formula(
                rule.formula_expression,
                calculated,
            )

            calculated[
                str(rule.formula_code)
            ] = output

        return calculated