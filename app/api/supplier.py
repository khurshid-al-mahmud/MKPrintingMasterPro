"""
Supplier API.

REST API endpoints
for Supplier Management.
"""

from fastapi import APIRouter, Depends

from app.api.dependencies.service import get_supplier_service
from app.schemas.supplier import (
    SupplierCreate,
    SupplierResponse,
    SupplierUpdate,
)
from app.services.supplier_service import SupplierService


router = APIRouter(
    prefix="/supplier",
    tags=["Supplier"],
)


@router.get(
    "/",
    response_model=list[SupplierResponse],
)
def get_all_suppliers(
    service: SupplierService = Depends(get_supplier_service),
):
    return service.get_all()


@router.get(
    "/{supplier_id}",
    response_model=SupplierResponse,
)
def get_supplier(
    supplier_id: int,
    service: SupplierService = Depends(get_supplier_service),
):
    return service.get_by_id(
        supplier_id,
    )


@router.post(
    "/",
    response_model=SupplierResponse,
)
def create_supplier(
    supplier: SupplierCreate,
    service: SupplierService = Depends(get_supplier_service),
):
    return service.create(
        supplier,
    )


@router.put(
    "/{supplier_id}",
    response_model=SupplierResponse,
)
def update_supplier(
    supplier_id: int,
    supplier: SupplierUpdate,
    service: SupplierService = Depends(get_supplier_service),
):
    return service.update(
        supplier_id,
        supplier,
    )


@router.delete(
    "/{supplier_id}",
)
def delete_supplier(
    supplier_id: int,
    service: SupplierService = Depends(get_supplier_service),
):
    return service.delete(
        supplier_id,
    )


@router.get(
    "/search/{keyword}",
    response_model=list[SupplierResponse],
)
def search_supplier(
    keyword: str,
    service: SupplierService = Depends(get_supplier_service),
):
    return service.search(
        keyword,
    )