"""
MKPrintingMasterPro ERP
Build-015A

Formula Rule Repository

Purpose:
Repository for FormulaRule CRUD operations.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.models.formula_rule import FormulaRule
from app.repositories.base_repository import BaseRepository


class FormulaRuleRepository(BaseRepository):
    """
    Formula Rule Repository
    """

    def __init__(self, db: Session):
        super().__init__(db, FormulaRule)

    # ------------------------------------------
    # Find by ID
    # ------------------------------------------

    def get_by_id(self, rule_id: int):
        return (
            self.db.query(FormulaRule)
            .filter(FormulaRule.id == rule_id)
            .first()
        )

    # ------------------------------------------
    # Find by Code
    # ------------------------------------------

    def get_by_code(self, formula_code: str):
        return (
            self.db.query(FormulaRule)
            .filter(
                FormulaRule.formula_code == formula_code
            )
            .first()
        )

    # ------------------------------------------
    # Get Active Rules
    # ------------------------------------------

    def get_active_rules(self):
        return (
            self.db.query(FormulaRule)
            .filter(
                FormulaRule.is_active.is_(True)
            )
            .order_by(
                FormulaRule.formula_name_en
            )
            .all()
        )

    # ------------------------------------------
    # Get Rules By Template
    # ------------------------------------------

    def get_by_template(self, template_id: int):
        return (
            self.db.query(FormulaRule)
            .filter(
                FormulaRule.template_id == template_id
            )
            .order_by(
                FormulaRule.formula_name_en
            )
            .all()
        )

    # ------------------------------------------
    # Create
    # ------------------------------------------

    def create_rule(self, rule: FormulaRule):
        self.db.add(rule)
        self.db.commit()
        self.db.refresh(rule)
        return rule

    # ------------------------------------------
    # Update
    # ------------------------------------------

    def update_rule(self):
        self.db.commit()

    # ------------------------------------------
    # Delete
    # ------------------------------------------

    def delete_rule(self, rule: FormulaRule):
        self.db.delete(rule)
        self.db.commit()