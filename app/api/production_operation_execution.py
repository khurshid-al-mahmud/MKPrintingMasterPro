"""
MKPrintingMasterPro ERP

Production Operation Execution API

Build-035
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.production_operation_execution import (
    ProductionOperationExecutionCreate,
    ProductionOperationExecutionUpdate,
    ProductionOperationExecutionResponse,
)

from app.services.production_operation_execution_service import (
    ProductionOperationExecutionService,
)


router = APIRouter(
    prefix="/production-operation-execution",
    tags=["Production Operation Execution"],
)


# ============================================================
# Create
# ============================================================

@router.post(
    "/",
    response_model=ProductionOperationExecutionResponse,
)
def create_production_operation_execution(
    data: ProductionOperationExecutionCreate,
    db: Session = Depends(get_db),
):
    service = ProductionOperationExecutionService(db)

    return service.create(data)


# ============================================================
# Get All
# ============================================================

@router.get(
    "/",
    response_model=list[ProductionOperationExecutionResponse],
)
def get_production_operation_executions(
    db: Session = Depends(get_db),
):
    service = ProductionOperationExecutionService(db)

    return service.get_all()


# ============================================================
# Get By ID
# ============================================================

@router.get(
    "/{execution_id}",
    response_model=ProductionOperationExecutionResponse,
)
def get_production_operation_execution(
    execution_id: int,
    db: Session = Depends(get_db),
):
    service = ProductionOperationExecutionService(db)

    execution = service.get_by_id(
        execution_id
    )

    if not execution:
        raise HTTPException(
            status_code=404,
            detail="Production Operation Execution not found",
        )

    return execution


# ============================================================
# Update
# ============================================================

@router.put(
    "/{execution_id}",
    response_model=ProductionOperationExecutionResponse,
)
def update_production_operation_execution(
    execution_id: int,
    data: ProductionOperationExecutionUpdate,
    db: Session = Depends(get_db),
):
    service = ProductionOperationExecutionService(db)

    execution = service.update(
        execution_id,
        data,
    )

    if not execution:
        raise HTTPException(
            status_code=404,
            detail="Production Operation Execution not found",
        )

    return execution


# ============================================================
# Delete
# ============================================================

@router.delete(
    "/{execution_id}",
)
def delete_production_operation_execution(
    execution_id: int,
    db: Session = Depends(get_db),
):
    service = ProductionOperationExecutionService(db)

    deleted = service.delete(
        execution_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Production Operation Execution not found",
        )

    return {
        "message": "Production Operation Execution deleted successfully"
    }