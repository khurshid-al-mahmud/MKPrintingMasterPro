"""
Formula Rule Service.

Business Logic Layer
for Formula Rule Management.
"""

from app.models.formula_rule import FormulaRule


class FormulaRuleService:
    """
    Service for Formula Rule.
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
        formula_data,
    ) -> FormulaRule:

        existing = self.repository.get_by_code(
            formula_data.formula_code,
        )

        if existing:
            raise ValueError(
                "Formula Code already exists."
            )

        formula = FormulaRule(
            template_id=formula_data.template_id,
            formula_code=formula_data.formula_code,
            formula_name_en=formula_data.formula_name_en,
            formula_name_bn=formula_data.formula_name_bn,
            description=formula_data.description,
            formula_type=formula_data.formula_type,
            formula_expression=formula_data.formula_expression,
            version=formula_data.version,
            effective_date=formula_data.effective_date,
            is_default=formula_data.is_default,
            is_active=formula_data.is_active,
            created_by="system",
            updated_by="system",
        )

        return self.repository.create_rule(
            formula,
        )

    # =====================================
    # GET ALL
    # =====================================

    def get_all(self):

        return self.repository.get_active_rules()

    # =====================================
    # GET BY ID
    # =====================================

    def get_by_id(
        self,
        formula_id: int,
    ):

        return self.repository.get_by_id(
            formula_id,
        )

    # =====================================
    # GET BY TEMPLATE
    # =====================================

    def get_by_template(
        self,
        template_id: int,
    ):

        return self.repository.get_by_template(
            template_id,
        )

    # =====================================
    # UPDATE
    # =====================================

    def update(
        self,
        formula_id: int,
        formula_data,
    ):

        formula = self.repository.get_by_id(
            formula_id,
        )

        if formula is None:
            return None

        data = formula_data.model_dump(
            exclude_unset=True,
        )

        for key, value in data.items():
            setattr(
                formula,
                key,
                value,
            )

        formula.updated_by = "system"

        self.repository.update_rule()

        return formula

    # =====================================
    # DELETE (Soft Delete)
    # =====================================

    def delete(
        self,
        formula_id: int,
    ):

        formula = self.repository.get_by_id(
            formula_id,
        )

        if formula is None:
            return False

        formula.is_active = False
        formula.updated_by = "system"

        self.repository.update_rule()

        return True