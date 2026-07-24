"""
MKPrintingMasterPro ERP
Build-015A

Specification Dependency Rule Repository

Purpose:
Repository for SpecificationDependencyRule CRUD operations.

Status:
Production Ready
"""

from sqlalchemy.orm import Session

from app.models.specification_dependency_rule import (
    SpecificationDependencyRule,
)
from app.repositories.base_repository import BaseRepository


class SpecificationDependencyRuleRepository(BaseRepository):
    """
    Specification Dependency Rule Repository
    """

    def __init__(self, db: Session):
        super().__init__(db, SpecificationDependencyRule)

    # ------------------------------------------
    # Find by ID
    # ------------------------------------------

    def get_by_id(self, rule_id: int):
        return (
            self.db.query(SpecificationDependencyRule)
            .filter(
                SpecificationDependencyRule.id == rule_id
            )
            .first()
        )

    # ------------------------------------------
    # Get Active Rules
    # ------------------------------------------

    def get_active_rules(self):
        return (
            self.db.query(SpecificationDependencyRule)
            .filter(
                SpecificationDependencyRule.is_active.is_(True)
            )
            .order_by(
                SpecificationDependencyRule.priority
            )
            .all()
        )

    # ------------------------------------------
    # Get Rules By Template
    # ------------------------------------------

    def get_by_template(self, template_id: int):
        return (
            self.db.query(SpecificationDependencyRule)
            .filter(
                SpecificationDependencyRule.template_id
                == template_id
            )
            .order_by(
                SpecificationDependencyRule.priority
            )
            .all()
        )

    # ------------------------------------------
    # Get Rules By Source Field
    # ------------------------------------------

    def get_by_source_field(self, field_id: int):
        return (
            self.db.query(SpecificationDependencyRule)
            .filter(
                SpecificationDependencyRule.source_field_id
                == field_id
            )
            .order_by(
                SpecificationDependencyRule.priority
            )
            .all()
        )

    # ------------------------------------------
    # Create
    # ------------------------------------------

    def create_rule(
        self,
        rule: SpecificationDependencyRule,
    ):
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

    def delete_rule(
        self,
        rule: SpecificationDependencyRule,
    ):
        self.db.delete(rule)
        self.db.commit()