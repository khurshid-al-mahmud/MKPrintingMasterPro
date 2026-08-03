"""
Product Template API.

REST API endpoints
for Product Template Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import get_product_template_service
from app.schemas.product_template import (
    ProductTemplateCreate,
    ProductTemplateResponse,
    ProductTemplateUpdate,
)
from app.services.product_template_service import ProductTemplateService


router = APIRouter(
    prefix="/product-template",
    tags=["Product Template"],
)


@router.get(
    "/",
    response_model=list[ProductTemplateResponse],
)
def get_all_templates(
    service: ProductTemplateService = Depends(
        get_product_template_service
    ),
):
    try:
        return service.get_all()

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================
# SEARCH MUST COME BEFORE /{template_id}
# ==========================

@router.get(
    "/search/{keyword}",
    response_model=list[ProductTemplateResponse],
)
def search_template(
    keyword: str,
    service: ProductTemplateService = Depends(
        get_product_template_service
    ),
):
    try:
        return service.search(keyword)

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.get(
    "/{template_id}",
    response_model=ProductTemplateResponse,
)
def get_template(
    template_id: int,
    service: ProductTemplateService = Depends(
        get_product_template_service
    ),
):
    try:
        template = service.get_by_id(template_id)

        if template is None:
            raise HTTPException(
                status_code=404,
                detail="Template not found.",
            )

        return template

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
    response_model=ProductTemplateResponse,
)
def create_template(
    template: ProductTemplateCreate,
    service: ProductTemplateService = Depends(
        get_product_template_service
    ),
):
    try:
        return service.create(template)

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
    "/{template_id}",
    response_model=ProductTemplateResponse,
)
def update_template(
    template_id: int,
    template: ProductTemplateUpdate,
    service: ProductTemplateService = Depends(
        get_product_template_service
    ),
):
    try:
        updated = service.update(
            template_id,
            template,
        )

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail="Template not found.",
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
    "/{template_id}",
)
def delete_template(
    template_id: int,
    service: ProductTemplateService = Depends(
        get_product_template_service
    ),
):
    try:
        deleted = service.delete(template_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Template not found.",
            )

        return {
            "message": "Product Template deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )