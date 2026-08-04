"""
MKPrintingMasterPro ERP
Build-015A

Specification Dependency Rule Service

Purpose:
Business Logic Layer for
Specification Dependency Rule Management.

Status:
Production Ready
"""

from app.models.specification_dependency_rule import (
    SpecificationDependencyRule,
)


class SpecificationDependencyRuleService:
    """
    Service for Specification Dependency Rule.
    """

    def __init__(
        self,
        repository,
    ):
        self.repository = repository


    # =====================================
    # CREATE
    # =====================================

    def create(
        self,
        rule_data,
    ) -> SpecificationDependencyRule:


        rule = SpecificationDependencyRule(

            template_id=rule_data.template_id,

            source_field_id=rule_data.source_field_id,

            trigger_value=rule_data.trigger_value,

            target_field_id=rule_data.target_field_id,

            action=rule_data.action,

            description=rule_data.description,

            priority=rule_data.priority,

            is_active=rule_data.is_active,

            created_by="system",

            updated_by="system",
        )


        return self.repository.create_rule(
            rule
        )



    # =====================================
    # GET ALL
    # =====================================

    def get_all(self):

        return (
            self.repository
            .get_active_rules()
        )



    # =====================================
    # GET BY ID
    # =====================================

    def get_by_id(
        self,
        rule_id: int,
    ):

        return (
            self.repository
            .get_by_id(rule_id)
        )



    # =====================================
    # GET BY TEMPLATE
    # =====================================

    def get_by_template(
        self,
        template_id: int,
    ):

        return (
            self.repository
            .get_by_template(
                template_id
            )
        )



    # =====================================
    # GET BY SOURCE FIELD
    # =====================================

    def get_by_source_field(
        self,
        field_id: int,
    ):

        return (
            self.repository
            .get_by_source_field(
                field_id
            )
        )



    # =====================================
    # UPDATE
    # =====================================

    def update(
        self,
        rule_id: int,
        rule_data,
    ):


        rule = (
            self.repository
            .get_by_id(rule_id)
        )


        if rule is None:
            return None



        data = rule_data.model_dump(
            exclude_unset=True
        )



        for key, value in data.items():

            setattr(
                rule,
                key,
                value
            )


        rule.updated_by = "system"



        self.repository.update_rule()


        return rule



    # =====================================
    # DELETE (Soft Delete)
    # =====================================

    def delete(
        self,
        rule_id: int,
    ):


        rule = (
            self.repository
            .get_by_id(rule_id)
        )


        if rule is None:
            return False



        rule.is_active = False

        rule.updated_by = "system"



        self.repository.update_rule()


        return True