"""
MKPrintingMasterPro ERP

Production Operation Execution History API

Build-035
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.production_operation_execution_history import (
    ProductionOperationExecutionHistoryResponse,
)

from app.services.production_operation_execution_history_service import (
    ProductionOperationExecutionHistoryService,
)


router = APIRouter(
    prefix="/production-operation-execution-history",
    tags=["Production Operation Execution History"],
)


service = ProductionOperationExecutionHistoryService()


# ============================================================
# Get History By Execution
# ============================================================

@router.get(
    "/execution/{execution_id}",
    response_model=list[
        ProductionOperationExecutionHistoryResponse
    ],
)
def get_execution_history(
    execution_id: int,
    db: Session = Depends(get_db),
):
    return service.get_by_execution(
        db,
        execution_id,
    )


# ============================================================
# Get History By ID
# ============================================================

@router.get(
    "/{history_id}",
    response_model=ProductionOperationExecutionHistoryResponse,
)
def get_execution_history_by_id(
    history_id: int,
    db: Session = Depends(get_db),
):
    history = service.get_by_id(
        db,
        history_id,
    )

    if not history:
        raise HTTPException(
            status_code=404,
            detail="Production Operation Execution History not found",
        )

    return history


# ============================================================
# Create History
# ============================================================

@router.post(
    "",
    response_model=ProductionOperationExecutionHistoryResponse,
    status_code=201,
)
def create_execution_history(
    execution_id: int,
    previous_status: str | None = None,
    new_status: str = "Pending",
    completed_quantity: float | None = None,
    reject_quantity: float | None = None,
    operator_name: str | None = None,
    remarks: str | None = None,
    db: Session = Depends(get_db),
):
    history = service.create(
        db=db,
        execution_id=execution_id,
        previous_status=previous_status,
        new_status=new_status,
        completed_quantity=completed_quantity,
        reject_quantity=reject_quantity,
        operator_name=operator_name,
        remarks=remarks,
    )

    db.commit()

    return history


# ============================================================
# Delete History
# ============================================================

@router.delete(
    "/{history_id}",
)
def delete_execution_history(
    history_id: int,
    db: Session = Depends(get_db),
):
    deleted = service.delete(
        db,
        history_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Production Operation Execution History not found",
        )

    db.commit()

    return {
        "message": "Production Operation Execution History deleted successfully"
    }