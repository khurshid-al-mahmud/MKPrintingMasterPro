"""
MKPrintingMasterPro ERP

Production Order API

Build-031
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.production_order import (
    ProductionOrderCreate,
    ProductionOrderUpdate,
    ProductionOrderResponse,
)

from app.services.production_order_service import (
    ProductionOrderService,
)


router = APIRouter(
    prefix="/production-orders",
    tags=["Production Orders"],
)


@router.post(
    "/",
    response_model=ProductionOrderResponse,
)
def create_production_order(
    data: ProductionOrderCreate,
    db: Session = Depends(get_db),
):

    service = ProductionOrderService(db)

    try:
        return service.create(
            production_order_no=data.production_order_no,
            production_order_date=data.production_order_date,
            job_order_id=data.job_order_id,
            status=data.status,
            priority=data.priority,
            planned_start_date=data.planned_start_date,
            planned_end_date=data.planned_end_date,
            remarks=data.remarks,
            created_by=data.created_by,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[ProductionOrderResponse],
)
def get_all_production_orders(
    db: Session = Depends(get_db),
):

    service = ProductionOrderService(db)

    return service.get_all()


@router.get(
    "/{production_order_id}",
    response_model=ProductionOrderResponse,
)
def get_production_order(
    production_order_id: int,
    db: Session = Depends(get_db),
):

    service = ProductionOrderService(db)

    production_order = service.get_by_id(
        production_order_id
    )

    if production_order is None:
        raise HTTPException(
            status_code=404,
            detail="Production Order not found.",
        )

    return production_order


@router.get(
    "/job-order/{job_order_id}",
    response_model=list[ProductionOrderResponse],
)
def get_production_orders_by_job_order(
    job_order_id: int,
    db: Session = Depends(get_db),
):

    service = ProductionOrderService(db)

    return service.get_by_job_order(
        job_order_id
    )


@router.put(
    "/{production_order_id}",
    response_model=ProductionOrderResponse,
)
def update_production_order(
    production_order_id: int,
    data: ProductionOrderUpdate,
    db: Session = Depends(get_db),
):

    service = ProductionOrderService(db)

    try:
        return service.update(
            production_order_id=production_order_id,
            production_order_date=data.production_order_date,
            job_order_id=data.job_order_id,
            status=data.status,
            priority=data.priority,
            planned_start_date=data.planned_start_date,
            planned_end_date=data.planned_end_date,
            remarks=data.remarks,
            updated_by=data.updated_by,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.delete(
    "/{production_order_id}",
)
def delete_production_order(
    production_order_id: int,
    db: Session = Depends(get_db),
):

    service = ProductionOrderService(db)

    try:
        service.delete(
            production_order_id
        )

        return {
            "message": "Production Order deleted successfully."
        }

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )