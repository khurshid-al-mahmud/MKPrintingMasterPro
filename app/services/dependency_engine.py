"""
MKPrintingMasterPro ERP
Build-016A

Dependency Engine

Purpose:
Enterprise Dynamic Dependency Runtime

Status:
Production Ready
"""

from typing import Dict, List

from app.repositories.specification_dependency_rule_repository import (
    SpecificationDependencyRuleRepository,
)


class DependencyEngine:

    def __init__(self, db):

        self.db = db

        self.repository = (
            SpecificationDependencyRuleRepository(db)
        )

    # --------------------------------------------------

    def get_rules(
        self,
        template_id: int,
    ):

        return self.repository.get_by_template(
            template_id
        )

    # --------------------------------------------------

    def evaluate(
        self,
        template_id: int,
        values: Dict,
    ):

        rules = self.get_rules(
            template_id
        )

        actions: List[Dict] = []

        for rule in rules:

            source_value = values.get(
                rule.source_field_id
            )

            if source_value is None:
                continue

            if str(source_value) != str(
                rule.trigger_value
            ):
                continue

            actions.append({

                "target_field_id":
                    rule.target_field_id,

                "action":
                    str(rule.action).upper(),

                "source_field_id":
                    rule.source_field_id,

                "trigger_value":
                    rule.trigger_value,

            })

        return actions

    # --------------------------------------------------

    def process(
        self,
        template_id: int,
        values: Dict,
        field_state: Dict,
    ):

        actions = self.evaluate(
            template_id,
            values,
        )

        state = self.apply_actions(
            field_state,
            actions,
        )

        return {

            "actions": actions,

            "field_state": state,

        }

    # --------------------------------------------------

    def apply_actions(
        self,
        field_state: Dict,
        actions: List[Dict],
    ):

        for action in actions:

            target = action[
                "target_field_id"
            ]

            if target not in field_state:
                continue

            current = field_state[target]

            command = action[
                "action"
            ]

            match command:

                case "SHOW":
                    current["visible"] = True

                case "HIDE":
                    current["visible"] = False

                case "ENABLE":
                    current["enabled"] = True

                case "DISABLE":
                    current["enabled"] = False

                case "REQUIRED":
                    current["required"] = True

                case "OPTIONAL":
                    current["required"] = False

                case "READONLY":
                    current["editable"] = False

                case "EDITABLE":
                    current["editable"] = True

        return field_state