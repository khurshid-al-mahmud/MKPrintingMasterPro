"""
MKPrintingMasterPro ERP
Build-015A

Formula Rule Repository

Purpose:
Repository for FormulaRule CRUD operations.
"""

from sqlalchemy.orm import Session

from app.models.formula_rule import FormulaRule


class FormulaRuleRepository:
    """
    Formula Rule Repository
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db


    # =====================================
    # CREATE
    # =====================================

    def create_rule(
        self,
        formula: FormulaRule,
    ) -> FormulaRule:

        self.db.add(formula)
        self.db.commit()
        self.db.refresh(formula)

        return formula


    # =====================================
    # GET ACTIVE RULES
    # =====================================

    def get_active_rules(self):

        return (
            self.db.query(
                FormulaRule
            )
            .filter(
                FormulaRule.is_active.is_(True)
            )
            .order_by(
                FormulaRule.formula_name_en
            )
            .all()
        )


    # =====================================
    # GET BY ID
    # =====================================

    def get_by_id(
        self,
        formula_id: int,
    ):

        return (
            self.db.query(
                FormulaRule
            )
            .filter(
                FormulaRule.id == formula_id
            )
            .first()
        )


    # =====================================
    # GET BY CODE
    # =====================================

    def get_by_code(
        self,
        formula_code: str,
    ):

        return (
            self.db.query(
                FormulaRule
            )
            .filter(
                FormulaRule.formula_code == formula_code
            )
            .first()
        )


    # =====================================
    # GET BY TEMPLATE
    # =====================================

    def get_by_template(
        self,
        template_id: int,
    ):

        return (
            self.db.query(
                FormulaRule
            )
            .filter(
                FormulaRule.template_id == template_id
            )
            .order_by(
                FormulaRule.formula_name_en
            )
            .all()
        )


    # =====================================
    # UPDATE
    # =====================================

    def update_rule(
        self,
    ):

        self.db.commit()


    # =====================================
    # DELETE (SOFT DELETE)
    # =====================================

    def delete_rule(
        self,
        formula: FormulaRule,
    ):

        setattr(
            formula,
            "is_active",
            False,
        )

        self.db.commit()

        return True