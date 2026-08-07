"""
MKPrintingMasterPro ERP

Production Output API

Build-034
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.production_output import (
    ProductionOutputCreate,
    ProductionOutputResponse,
    ProductionOutputUpdate,
)

from app.services.production_output_service import (
    ProductionOutputService,
)


router = APIRouter(
    prefix="/production-output",
    tags=["Production Output"],
)


service = ProductionOutputService()


# ==========================
# Create Production Output
# ==========================

@router.post(
    "/",
    response_model=ProductionOutputResponse,
)
def create_production_output(
    data: ProductionOutputCreate,
    db: Session = Depends(get_db),
):

    return service.create_output(
        db,
        data,
    )


# ==========================
# Get All
# ==========================

@router.get(
    "/",
    response_model=list[ProductionOutputResponse],
)
def get_production_outputs(
    db: Session = Depends(get_db),
):

    return service.get_outputs(
        db,
    )


# ==========================
# Get By ID
# ==========================

@router.get(
    "/{output_id}",
    response_model=ProductionOutputResponse,
)
def get_production_output(
    output_id: int,
    db: Session = Depends(get_db),
):

    output = service.get_output(
        db,
        output_id,
    )

    if not output:
        raise HTTPException(
            status_code=404,
            detail="Production Output not found",
        )

    return output


# ==========================
# Update
# ==========================

@router.put(
    "/{output_id}",
    response_model=ProductionOutputResponse,
)
def update_production_output(
    output_id: int,
    data: ProductionOutputUpdate,
    db: Session = Depends(get_db),
):

    output = service.update_output(
        db,
        output_id,
        data,
    )

    if not output:
        raise HTTPException(
            status_code=404,
            detail="Production Output not found",
        )

    return output


# ==========================
# Delete
# ==========================

@router.delete(
    "/{output_id}",
)
def delete_production_output(
    output_id: int,
    db: Session = Depends(get_db),
):

    deleted = service.delete_output(
        db,
        output_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Production Output not found",
        )

    return {
        "message": "Production Output deleted successfully"
    }