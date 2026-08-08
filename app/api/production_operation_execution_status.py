"""
MKPrintingMasterPro ERP

Production Operation Execution Status API

Build-035
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.engine import get_db
from app.schemas.production_operation_execution_status import (
    ProductionOperationExecutionStatusCreate,
    ProductionOperationExecutionStatusResponse,
    ProductionOperationExecutionStatusUpdate,
)
from app.services.production_operation_execution_status_service import (
    ProductionOperationExecutionStatusService,
)


router = APIRouter(
    prefix="/production-operation-execution-status",
    tags=["Production Operation Execution Status"],
)

service = ProductionOperationExecutionStatusService()


@router.get(
    "",
    response_model=list[
        ProductionOperationExecutionStatusResponse
    ],
)
def get_statuses(
    active_only: bool = Query(False),
    db: Session = Depends(get_db),
):
    return service.get_all(
        db,
        active_only=active_only,
    )


@router.get(
    "/{status_id}",
    response_model=ProductionOperationExecutionStatusResponse,
)
def get_status(
    status_id: int,
    db: Session = Depends(get_db),
):
    status = service.get_by_id(
        db,
        status_id,
    )

    if not status:
        raise HTTPException(
            status_code=404,
            detail="Production Operation Execution Status not found",
        )

    return status


@router.post(
    "",
    response_model=ProductionOperationExecutionStatusResponse,
    status_code=201,
)
def create_status(
    data: ProductionOperationExecutionStatusCreate,
    db: Session = Depends(get_db),
):
    try:
        status = service.create(
            db,
            data,
        )

        db.commit()

        return status

    except ValueError as exc:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail=str(exc),
        )


@router.put(
    "/{status_id}",
    response_model=ProductionOperationExecutionStatusResponse,
)
def update_status(
    status_id: int,
    data: ProductionOperationExecutionStatusUpdate,
    db: Session = Depends(get_db),
):
    status = service.update(
        db,
        status_id,
        data,
    )

    if not status:
        raise HTTPException(
            status_code=404,
            detail="Production Operation Execution Status not found",
        )

    db.commit()

    return status


@router.delete(
    "/{status_id}",
)
def delete_status(
    status_id: int,
    db: Session = Depends(get_db),
):
    deleted = service.delete(
        db,
        status_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Production Operation Execution Status not found",
        )

    db.commit()

    return {
        "message": "Production Operation Execution Status deleted successfully"
    }

