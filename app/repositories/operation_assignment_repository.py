"""
MKPrintingMasterPro ERP

Operation Assignment Repository

Build-032
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.operation_assignment import OperationAssignment
from app.schemas.operation_assignment import (
    OperationAssignmentCreate,
    OperationAssignmentUpdate,
)


class OperationAssignmentRepository:

    def create(
        self,
        db: Session,
        data: OperationAssignmentCreate
    ) -> OperationAssignment:

        obj = OperationAssignment(
            **data.model_dump()
        )

        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj


    def get_by_id(
        self,
        db: Session,
        assignment_id: int
    ) -> Optional[OperationAssignment]:

        return (
            db.query(OperationAssignment)
            .filter(
                OperationAssignment.id == assignment_id
            )
            .first()
        )


    def get_all(
        self,
        db: Session
    ) -> List[OperationAssignment]:

        return (
            db.query(OperationAssignment)
            .order_by(
                OperationAssignment.sequence_no
            )
            .all()
        )


    def get_by_production_order(
        self,
        db: Session,
        production_order_id: int
    ) -> List[OperationAssignment]:

        return (
            db.query(OperationAssignment)
            .filter(
                OperationAssignment.production_order_id
                == production_order_id
            )
            .order_by(
                OperationAssignment.sequence_no
            )
            .all()
        )


    def update(
        self,
        db: Session,
        assignment_id: int,
        data: OperationAssignmentUpdate
    ) -> Optional[OperationAssignment]:

        obj = self.get_by_id(
            db,
            assignment_id
        )

        if not obj:
            return None


        update_data = data.model_dump(
            exclude_unset=True
        )


        for key, value in update_data.items():

            setattr(
                obj,
                key,
                value
            )


        db.commit()
        db.refresh(obj)

        return obj


    def delete(
        self,
        db: Session,
        assignment_id: int
    ) -> bool:

        obj = self.get_by_id(
            db,
            assignment_id
        )

        if not obj:
            return False


        db.delete(obj)
        db.commit()

        return True