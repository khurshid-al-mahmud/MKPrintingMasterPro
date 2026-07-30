"""
Product Category API.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import get_product_category_service
from app.schemas.product_category import (
    ProductCategoryCreate,
    ProductCategoryResponse,
    ProductCategoryUpdate,
)
from app.services.product_category_service import ProductCategoryService

router = APIRouter(
    prefix="/product-category",
    tags=["Product Category"],
)


@router.get("/", response_model=list[ProductCategoryResponse])
def get_all(
    service: ProductCategoryService = Depends(get_product_category_service),
):
    return service.get_all()


@router.get("/{category_id}", response_model=ProductCategoryResponse)
def get_by_id(
    category_id: int,
    service: ProductCategoryService = Depends(get_product_category_service),
):
    category = service.get_by_id(category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("/", response_model=ProductCategoryResponse)
def create(
    category: ProductCategoryCreate,
    service: ProductCategoryService = Depends(get_product_category_service),
):
    try:
        return service.create(category)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{category_id}", response_model=ProductCategoryResponse)
def update(
    category_id: int,
    category: ProductCategoryUpdate,
    service: ProductCategoryService = Depends(get_product_category_service),
):
    try:
        updated = service.update(category_id, category)

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail="Category not found",
            )

        return updated

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


@router.delete("/{category_id}")
def delete(
    category_id: int,
    service: ProductCategoryService = Depends(get_product_category_service),
):
    try:
        deleted = service.delete(category_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Category not found",
            )

        return {
            "message": "Deleted successfully."
        }

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )