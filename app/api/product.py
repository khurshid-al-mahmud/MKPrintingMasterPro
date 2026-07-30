"""
Product API.

REST API endpoints
for Product Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

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
    service: ProductService = Depends(get_product_service),
):
    try:
        return service.get_all()

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_product(
    product_id: int,
    service: ProductService = Depends(get_product_service),
):
    try:
        product = service.get_by_id(product_id)

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found.",
            )

        return product

    except HTTPException:
        raise

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=ProductResponse,
)
def create_product(
    product: ProductCreate,
    service: ProductService = Depends(get_product_service),
):
    try:
        return service.create(product)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product(
    product_id: int,
    product: ProductUpdate,
    service: ProductService = Depends(get_product_service),
):
    try:
        updated = service.update(
            product_id,
            product,
        )

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found.",
            )

        return updated

    except HTTPException:
        raise

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.delete(
    "/{product_id}",
)
def delete_product(
    product_id: int,
    service: ProductService = Depends(get_product_service),
):
    try:
        deleted = service.delete(product_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Product not found.",
            )

        return {
            "message": "Product deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get(
    "/search/{keyword}",
    response_model=list[ProductResponse],
)
def search_product(
    keyword: str,
    service: ProductService = Depends(get_product_service),
):
    try:
        return service.search(keyword)

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )