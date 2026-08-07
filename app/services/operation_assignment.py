"""
MKPrintingMasterPro ERP

Operation Assignment Service

Build-032
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.repositories.operation_assignment import (
    operation_assignment_repository,
)

from app.schemas.operation_assignment import (
    OperationAssignmentCreate,
    OperationAssignmentUpdate,
)


class OperationAssignmentService:
    """
    Service layer for Operation Assignment.
    """

    def create_operation_assignment(
        self,
        db: Session,
        assignment: OperationAssignmentCreate,
    ):
        return operation_assignment_repository.create(
            db=db,
            assignment=assignment,
        )

    def get_operation_assignment(
        self,
        db: Session,
        assignment_id: int,
    ):
        return operation_assignment_repository.get_by_id(
            db=db,
            assignment_id=assignment_id,
        )

    def get_all_operation_assignments(
        self,
        db: Session,
    ) -> List:
        return operation_assignment_repository.get_all(
            db=db,
        )

    def get_operation_assignments_by_production_order(
        self,
        db: Session,
        production_order_id: int,
    ):
        return (
            operation_assignment_repository
            .get_by_production_order(
                db=db,
                production_order_id=production_order_id,
            )
        )

    def update_operation_assignment(
        self,
        db: Session,
        assignment_id: int,
        assignment: OperationAssignmentUpdate,
    ):
        db_assignment = (
            operation_assignment_repository.get_by_id(
                db=db,
                assignment_id=assignment_id,
            )
        )

        if not db_assignment:
            return None

        return operation_assignment_repository.update(
            db=db,
            db_assignment=db_assignment,
            assignment=assignment,
        )

    def delete_operation_assignment(
        self,
        db: Session,
        assignment_id: int,
    ):
        db_assignment = (
            operation_assignment_repository.get_by_id(
                db=db,
                assignment_id=assignment_id,
            )
        )

        if not db_assignment:
            return False

        return operation_assignment_repository.delete(
            db=db,
            db_assignment=db_assignment,
        )


operation_assignment_service = OperationAssignmentService()