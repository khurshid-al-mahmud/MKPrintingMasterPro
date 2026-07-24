"""
MKPrintingMasterPro ERP
Build-016A

Formula Engine

Purpose:
Enterprise Dynamic Formula Runtime

Status:
Production Ready
"""

from typing import Dict, List

from sqlalchemy.orm import Session

from app.repositories.formula_rule_repository import (
    FormulaRuleRepository,
)


class FormulaEngine:

    def __init__(self, db: Session):

        self.db = db

        self.repository = FormulaRuleRepository(db)

    # --------------------------------------------------

    def get_rules(
        self,
        template_id: int,
    ):

        return self.repository.get_by_template(
            template_id
        )

    # --------------------------------------------------

    def execute_formula(
        self,
        expression: str,
        values: Dict,
    ):

        safe_globals = {

            "__builtins__": {},

            "min": min,

            "max": max,

            "round": round,

            "abs": abs,

            "int": int,

            "float": float,

            "sum": sum,

            "len": len,

        }

        try:

            return eval(

                str(expression),

                safe_globals,

                values,

            )

        except Exception as ex:

            return {

                "error": str(ex)

            }

    # --------------------------------------------------

    def calculate_single(

        self,

        rule,

        values: Dict,

    ):

        return self.execute_formula(

            str(rule.formula_expression),

            values,

        )

    # --------------------------------------------------

    def calculate(

        self,

        template_id: int,

        values: Dict,

    ):

        rules = self.get_rules(

            template_id

        )

        result = {}

        for rule in rules:

            output = self.calculate_single(

                rule,

                values,

            )

            result[

                str(rule.formula_code)

            ] = output

        return result

    # --------------------------------------------------

    def calculate_all(

        self,

        template_id: int,

        values: Dict,

    ):

        calculated = values.copy()

        formula_log: List[Dict] = []

        rules = self.get_rules(

            template_id

        )

        for rule in rules:

            output = self.calculate_single(

                rule,

                calculated,

            )

            calculated[

                str(rule.formula_code)

            ] = output

            formula_log.append({

                "formula_code":

                    str(rule.formula_code),

                "expression":

                    str(rule.formula_expression),

                "result":

                    output,

            })

        return {

            "values": calculated,

            "log": formula_log,

        }