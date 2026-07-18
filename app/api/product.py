"""
Product API.

REST API endpoints
for Product Management.
"""

from fastapi import APIRouter, Depends

from app.api.dependencies.service import get_product_service
from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/product",
    tags=["Product"],
)


@router.get(
    "/",
    response_model=list[ProductResponse],
)
def get_all_products(
    service: ProductService = Depends(
        get_product_service,
    ),
):
    """
    Get all products.
    """

    return service.get_all()


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_product(
    product_id: int,
    service: ProductService = Depends(
        get_product_service,
    ),
):
    """
    Get product by ID.
    """

    return service.get_by_id(
        product_id,
    )


@router.post(
    "/",
    response_model=ProductResponse,
)
def create_product(
    product: ProductCreate,
    service: ProductService = Depends(
        get_product_service,
    ),
):
    """
    Create product.
    """

    return service.create(
        product,
    )


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product(
    product_id: int,
    product: ProductUpdate,
    service: ProductService = Depends(
        get_product_service,
    ),
):
    """
    Update product.
    """

    return service.update(
        product_id,
        product,
    )


@router.delete(
    "/{product_id}",
)
def delete_product(
    product_id: int,
    service: ProductService = Depends(
        get_product_service,
    ),
):
    """
    Soft delete product.
    """

    return service.delete(
        product_id,
    )


@router.get(
    "/search/{keyword}",
    response_model=list[ProductResponse],
)
def search_product(
    keyword: str,
    service: ProductService = Depends(
        get_product_service,
    ),
):
    """
    Search products.
    """

    return service.search(
        keyword,
    )