"""
MKPrintingMasterPro ERP

Operation Master API

Build-031
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.operation_master import (
    OperationMasterCreate,
    OperationMasterUpdate,
    OperationMasterResponse,
)
from app.services.operation_master import OperationMasterService


router = APIRouter(
    prefix="/operation-master",
    tags=["Operation Master"],
)


# ==========================================================
# Create Operation
# ==========================================================

@router.post(
    "",
    response_model=OperationMasterResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_operation(
    data: OperationMasterCreate,
    db: Session = Depends(get_db),
):
    service = OperationMasterService(db)

    try:
        return service.create(
            operation_code=data.operation_code,
            operation_name=data.operation_name,
            description=data.description,
            display_order=data.display_order,
            is_active=data.is_active,
            created_by=data.created_by,
            updated_by=data.updated_by,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


# ==========================================================
# Get Operation by ID
# ==========================================================

@router.get(
    "/{operation_id}",
    response_model=OperationMasterResponse,
)
def get_operation(
    operation_id: int,
    db: Session = Depends(get_db),
):
    service = OperationMasterService(db)

    operation = service.get_by_id(operation_id)

    if operation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operation not found.",
        )

    return operation


# ==========================================================
# Get Operation by Code
# ==========================================================

@router.get(
    "/code/{operation_code}",
    response_model=OperationMasterResponse,
)
def get_operation_by_code(
    operation_code: str,
    db: Session = Depends(get_db),
):
    service = OperationMasterService(db)

    operation = service.get_by_code(operation_code)

    if operation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Operation not found.",
        )

    return operation


# ==========================================================
# Get All Operations
# ==========================================================

@router.get(
    "",
    response_model=list[OperationMasterResponse],
)
def get_all_operations(
    db: Session = Depends(get_db),
):
    service = OperationMasterService(db)

    return service.get_all()


# ==========================================================
# Get Active Operations
# ==========================================================

@router.get(
    "/active/list",
    response_model=list[OperationMasterResponse],
)
def get_active_operations(
    db: Session = Depends(get_db),
):
    service = OperationMasterService(db)

    return service.get_active()


# ==========================================================
# Update Operation
# ==========================================================

@router.put(
    "/{operation_id}",
    response_model=OperationMasterResponse,
)
def update_operation(
    operation_id: int,
    data: OperationMasterUpdate,
    db: Session = Depends(get_db),
):
    service = OperationMasterService(db)

    try:
        return service.update(
            operation_id=operation_id,
            operation_code=data.operation_code,
            operation_name=data.operation_name,
            description=data.description,
            display_order=data.display_order,
            is_active=data.is_active,
            updated_by=data.updated_by,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )


# ==========================================================
# Delete Operation
# ==========================================================

@router.delete(
    "/{operation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_operation(
    operation_id: int,
    db: Session = Depends(get_db),
):
    service = OperationMasterService(db)

    try:
        service.delete(operation_id)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

    return None