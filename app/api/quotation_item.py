"""
Quotation Item API.

REST API endpoints
for Quotation Item Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import (
    get_quotation_item_service,
)

from app.schemas.quotation_item import (
    QuotationItemCreate,
    QuotationItemResponse,
    QuotationItemUpdate,
)

from app.services.quotation_item_service import (
    QuotationItemService,
)


router = APIRouter(
    prefix="/quotation-item",
    tags=["Quotation Item"],
)


@router.get(
    "/",
    response_model=list[QuotationItemResponse],
)
def get_all_items(
    service: QuotationItemService = Depends(
        get_quotation_item_service
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


@router.get(
    "/{item_id}",
    response_model=QuotationItemResponse,
)
def get_item(
    item_id: int,
    service: QuotationItemService = Depends(
        get_quotation_item_service
    ),
):
    try:
        item = service.get_by_id(
            item_id,
        )

        if item is None:
            raise HTTPException(
                status_code=404,
                detail="Quotation Item not found.",
            )

        return item

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
    response_model=QuotationItemResponse,
)
def create_item(
    item: QuotationItemCreate,
    service: QuotationItemService = Depends(
        get_quotation_item_service
    ),
):
    try:
        return service.create(
            item,
        )

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.put(
    "/{item_id}",
    response_model=QuotationItemResponse,
)
def update_item(
    item_id: int,
    item: QuotationItemUpdate,
    service: QuotationItemService = Depends(
        get_quotation_item_service
    ),
):
    try:
        updated = service.update(
            item_id,
            item,
        )

        if updated is None:
            raise HTTPException(
                status_code=404,
                detail="Quotation Item not found.",
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
    "/{item_id}",
)
def delete_item(
    item_id: int,
    service: QuotationItemService = Depends(
        get_quotation_item_service
    ),
):
    try:
        deleted = service.delete(
            item_id,
        )

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Quotation Item not found.",
            )

        return {
            "message": "Quotation Item deleted successfully."
        }

    except HTTPException:
        raise

    except Exception as e:
        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )