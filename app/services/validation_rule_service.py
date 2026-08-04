"""
MKPrintingMasterPro ERP

Build-013

Validation Rule Service

Purpose:
Business Logic Layer
for Validation Rule Management.

Status:
Production Ready
"""


from app.models.validation_rule import ValidationRule


class ValidationRuleService:
    """
    Validation Rule Service.
    """

    def __init__(self, repository):
        self.repository = repository


    # ==================================================
    # CREATE
    # ==================================================

    def create(
        self,
        rule_data,
    ) -> ValidationRule:

        existing = self.repository.get_by_code(
            rule_data.rule_code
        )

        if existing:
            raise ValueError(
                "Validation Rule Code already exists."
            )


        rule = ValidationRule(

            field_id=rule_data.field_id,

            rule_code=rule_data.rule_code,

            rule_name=rule_data.rule_name,

            description=rule_data.description,

            validation_type=rule_data.validation_type,

            minimum_value=rule_data.minimum_value,

            maximum_value=rule_data.maximum_value,

            regex_pattern=rule_data.regex_pattern,

            validation_expression=(
                rule_data.validation_expression
            ),

            error_message=(
                rule_data.error_message
            ),

            stop_processing=(
                rule_data.stop_processing
            ),

            is_active=(
                rule_data.is_active
            ),

            created_by="system",

            updated_by="system",
        )


        return self.repository.create_rule(rule)



    # ==================================================
    # GET ALL ACTIVE
    # ==================================================

    def get_all(self):

        return self.repository.get_active_rules()



    # ==================================================
    # GET BY ID
    # ==================================================

    def get_by_id(
        self,
        rule_id: int,
    ):

        return self.repository.get_by_id(
            rule_id
        )



    # ==================================================
    # GET BY FIELD
    # ==================================================

    def get_by_field(
        self,
        field_id: int,
    ):

        return self.repository.get_by_field(
            field_id
        )



    # ==================================================
    # UPDATE
    # ==================================================

    def update(
        self,
        rule_id: int,
        rule_data,
    ):

        rule = self.repository.get_by_id(
            rule_id
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
                value,
            )


        rule.updated_by = "system"


        self.repository.db.commit()

        self.repository.db.refresh(rule)


        return rule



    # ==================================================
    # DELETE (Soft Delete)
    # ==================================================

    def delete(
        self,
        rule_id: int,
    ):

        rule = self.repository.get_by_id(
            rule_id
        )


        if rule is None:
            return False


        rule.is_active = False

        rule.updated_by = "system"


        self.repository.db.commit()


        return True