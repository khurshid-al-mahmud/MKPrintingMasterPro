"""
MKPrintingMasterPro ERP

Operation Assignment Repository

Build-032
"""

from typing import List, Optional

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.operation_assignment import OperationAssignment
from app.schemas.operation_assignment import (
    OperationAssignmentCreate,
    OperationAssignmentUpdate,
)


class OperationAssignmentRepository:
    """Repository for Operation Assignment database operations."""

    def get_all(
        self,
        db: Session,
    ) -> List[OperationAssignment]:
        return (
            db.query(OperationAssignment)
            .order_by(
                OperationAssignment.production_order_id.asc(),
                OperationAssignment.sequence_no.asc(),
                OperationAssignment.id.asc(),
            )
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        assignment_id: int,
    ) -> Optional[OperationAssignment]:
        return (
            db.query(OperationAssignment)
            .filter(
                OperationAssignment.id == assignment_id
            )
            .first()
        )

    def get_by_production_order(
        self,
        db: Session,
        production_order_id: int,
    ) -> List[OperationAssignment]:
        return (
            db.query(OperationAssignment)
            .filter(
                OperationAssignment.production_order_id
                == production_order_id
            )
            .order_by(
                OperationAssignment.sequence_no.asc(),
                OperationAssignment.id.asc(),
            )
            .all()
        )

    def get_by_order_operation_sequence(
        self,
        db: Session,
        production_order_id: int,
        operation_id: int,
        sequence_no: int,
    ) -> Optional[OperationAssignment]:
        """
        Find an existing assignment using the unique business key.
        """

        return (
            db.query(OperationAssignment)
            .filter(
                OperationAssignment.production_order_id
                == production_order_id,
                OperationAssignment.operation_id
                == operation_id,
                OperationAssignment.sequence_no
                == sequence_no,
            )
            .first()
        )

    def create(
        self,
        db: Session,
        assignment: OperationAssignmentCreate,
    ) -> OperationAssignment:
        """
        Create a new operation assignment.

        Database-level unique constraint is the final
        protection against duplicate assignments.
        """

        db_assignment = OperationAssignment(
            **assignment.model_dump()
        )

        db.add(db_assignment)

        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise

        db.refresh(db_assignment)

        return db_assignment

    def update(
        self,
        db: Session,
        db_assignment: OperationAssignment,
        assignment: OperationAssignmentUpdate,
    ) -> OperationAssignment:
        """
        Update an existing operation assignment.
        """

        update_data = assignment.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_assignment,
                key,
                value,
            )

        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise

        db.refresh(db_assignment)

        return db_assignment

    def delete(
        self,
        db: Session,
        db_assignment: OperationAssignment,
    ) -> bool:
        """
        Delete an operation assignment.
        """

        db.delete(db_assignment)

        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise

        return True


operation_assignment_repository = OperationAssignmentRepository()