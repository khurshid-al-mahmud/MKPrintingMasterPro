"""
MKPrintingMasterPro ERP
Build-015A

Validation Rule Repository

Purpose:
Repository for ValidationRule CRUD operations.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.models.validation_rule import ValidationRule
from app.repositories.base_repository import BaseRepository


class ValidationRuleRepository(BaseRepository):
    """
    Validation Rule Repository
    """

    def __init__(self, db: Session):
        super().__init__(db, ValidationRule)

    # ------------------------------------------
    # Find by ID
    # ------------------------------------------

    def get_by_id(self, rule_id: int):
        return (
            self.db.query(ValidationRule)
            .filter(ValidationRule.id == rule_id)
            .first()
        )

    # ------------------------------------------
    # Find by Code
    # ------------------------------------------

    def get_by_code(self, rule_code: str):
        return (
            self.db.query(ValidationRule)
            .filter(
                ValidationRule.rule_code == rule_code
            )
            .first()
        )

    # ------------------------------------------
    # Get Active Rules
    # ------------------------------------------

    def get_active_rules(self):
        return (
            self.db.query(ValidationRule)
            .filter(
                ValidationRule.is_active.is_(True)
            )
            .order_by(
                ValidationRule.rule_name
            )
            .all()
        )

    # ------------------------------------------
    # Get Rules By Field
    # ------------------------------------------

    def get_by_field(self, field_id: int):
        return (
            self.db.query(ValidationRule)
            .filter(
                ValidationRule.field_id == field_id
            )
            .order_by(
                ValidationRule.rule_name
            )
            .all()
        )

    # ------------------------------------------
    # Create
    # ------------------------------------------

    def create_rule(self, rule: ValidationRule):
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

    def delete_rule(self, rule: ValidationRule):
        self.db.delete(rule)
        self.db.commit()