"""
Invoice Item API.

REST API endpoints
for Invoice Item Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import (
    get_invoice_item_service,
)

from app.services.invoice_item_service import (
    InvoiceItemService,
)

from app.schemas.invoice_item import (
    InvoiceItemCreate,
    InvoiceItemUpdate,
    InvoiceItemResponse,
)



router = APIRouter(
    prefix="/invoice-item",
    tags=["Invoice Item"],
)



# ======================================
# GET ALL INVOICE ITEMS
# ======================================

@router.get(
    "/",
    response_model=list[InvoiceItemResponse],
)
def get_all_invoice_items(
    service: InvoiceItemService = Depends(
        get_invoice_item_service
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



# ======================================
# GET SINGLE INVOICE ITEM
# ======================================

@router.get(
    "/{item_id}",
    response_model=InvoiceItemResponse,
)
def get_invoice_item(
    item_id: int,
    service: InvoiceItemService = Depends(
        get_invoice_item_service
    ),
):

    try:

        item = service.get_by_id(
            item_id
        )


        if item is None:

            raise HTTPException(
                status_code=404,
                detail="Invoice Item not found.",
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



# ======================================
# CREATE INVOICE ITEM
# ======================================

@router.post(
    "/",
    response_model=InvoiceItemResponse,
)
def create_invoice_item(
    item: InvoiceItemCreate,
    service: InvoiceItemService = Depends(
        get_invoice_item_service
    ),
):

    try:

        return service.create(
            item.model_dump()
        )


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ======================================
# UPDATE INVOICE ITEM
# ======================================

@router.put(
    "/{item_id}",
    response_model=InvoiceItemResponse,
)
def update_invoice_item(
    item_id: int,
    item: InvoiceItemUpdate,
    service: InvoiceItemService = Depends(
        get_invoice_item_service
    ),
):

    try:

        updated_item = service.update(
            item_id,
            item.model_dump(
                exclude_unset=True
            ),
        )


        if updated_item is None:

            raise HTTPException(
                status_code=404,
                detail="Invoice Item not found.",
            )


        return updated_item


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ======================================
# DELETE INVOICE ITEM
# ======================================

@router.delete("/{item_id}")
def delete_invoice_item(
    item_id: int,
    service: InvoiceItemService = Depends(
        get_invoice_item_service
    ),
):

    try:

        deleted = service.delete(
            item_id
        )


        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Invoice Item not found.",
            )


        return {
            "message": "Invoice Item deleted successfully."
        }


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )