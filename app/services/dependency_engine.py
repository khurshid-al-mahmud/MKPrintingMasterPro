"""
MKPrintingMasterPro ERP
Build-015B

Dependency Engine

Purpose:
Handles Dynamic Specification
Dependency Rules.

Status:
Production Ready
"""

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
        values: dict,
    ):

        rules = self.get_rules(template_id)

        result = []

        for rule in rules:

            source_value = values.get(
                rule.source_field_id
            )

            if str(source_value) == str(
                rule.trigger_value
            ):

                result.append(

                    {

                        "target_field_id": rule.target_field_id,

                        "action": rule.action,

                        "source_field_id": rule.source_field_id,

                        "trigger_value": rule.trigger_value,

                    }

                )

        return result

    # --------------------------------------------------

    def apply_actions(
        self,
        field_state: dict,
        actions: list,
    ):

        for action in actions:

            target = action["target_field_id"]

            if target not in field_state:

                continue

            rule_action = action["action"].upper()

            if rule_action == "SHOW":

                field_state[target]["visible"] = True

            elif rule_action == "HIDE":

                field_state[target]["visible"] = False

            elif rule_action == "ENABLE":

                field_state[target]["enabled"] = True

            elif rule_action == "DISABLE":

                field_state[target]["enabled"] = False

            elif rule_action == "REQUIRED":

                field_state[target]["required"] = True

            elif rule_action == "OPTIONAL":

                field_state[target]["required"] = False

            elif rule_action == "READONLY":

                field_state[target]["editable"] = False

        return field_state