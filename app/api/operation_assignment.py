"""
MKPrintingMasterPro ERP

Operation Assignment API

Build-032
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.operation_assignment import (
    OperationAssignmentCreate,
    OperationAssignmentUpdate,
    OperationAssignmentResponse,
)

from app.services.operation_assignment import (
    operation_assignment_service,
)


router = APIRouter(
    prefix="/operation-assignment",
    tags=["Operation Assignment"],
)


@router.post(
    "/",
    response_model=OperationAssignmentResponse,
)
def create_operation_assignment(
    assignment: OperationAssignmentCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new Operation Assignment.

    Duplicate combination of:
    production_order_id + operation_id + sequence_no
    is rejected with HTTP 409.
    """

    try:
        return operation_assignment_service.create_operation_assignment(
            db=db,
            assignment=assignment,
        )

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail=(
                "Operation Assignment already exists for this "
                "Production Order, Operation and Sequence No."
            ),
        )


@router.get(
    "/{assignment_id}",
    response_model=OperationAssignmentResponse,
)
def get_operation_assignment(
    assignment_id: int,
    db: Session = Depends(get_db),
):
    result = operation_assignment_service.get_operation_assignment(
        db=db,
        assignment_id=assignment_id,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Operation Assignment not found",
        )

    return result


@router.get(
    "/",
    response_model=List[OperationAssignmentResponse],
)
def get_all_operation_assignments(
    db: Session = Depends(get_db),
):
    return operation_assignment_service.get_all_operation_assignments(
        db=db,
    )


@router.get(
    "/production-order/{production_order_id}",
    response_model=List[OperationAssignmentResponse],
)
def get_by_production_order(
    production_order_id: int,
    db: Session = Depends(get_db),
):
    return (
        operation_assignment_service
        .get_operation_assignments_by_production_order(
            db=db,
            production_order_id=production_order_id,
        )
    )


@router.put(
    "/{assignment_id}",
    response_model=OperationAssignmentResponse,
)
def update_operation_assignment(
    assignment_id: int,
    assignment: OperationAssignmentUpdate,
    db: Session = Depends(get_db),
):
    try:
        result = operation_assignment_service.update_operation_assignment(
            db=db,
            assignment_id=assignment_id,
            assignment=assignment,
        )

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="Operation Assignment not found",
            )

        return result

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail=(
                "Operation Assignment already exists for this "
                "Production Order, Operation and Sequence No."
            ),
        )


@router.delete(
    "/{assignment_id}",
)
def delete_operation_assignment(
    assignment_id: int,
    db: Session = Depends(get_db),
):
    result = operation_assignment_service.delete_operation_assignment(
        db=db,
        assignment_id=assignment_id,
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Operation Assignment not found",
        )

    return {
        "message": "Operation Assignment deleted successfully",
    }