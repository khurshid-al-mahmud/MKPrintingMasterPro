"""
Invoice API.

REST API endpoints
for Invoice Master Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import (
    get_invoice_service,
)

from app.services.invoice_service import (
    InvoiceService,
)

from app.schemas.invoice import (
    InvoiceCreate,
    InvoiceUpdate,
    InvoiceResponse,
)


router = APIRouter(
    prefix="/invoice",
    tags=["Invoice Master"],
)



# ======================================
# GET ALL INVOICES
# ======================================

@router.get(
    "/",
    response_model=list[InvoiceResponse],
)
def get_all_invoices(
    service: InvoiceService = Depends(
        get_invoice_service
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
# GET SINGLE INVOICE
# ======================================

@router.get(
    "/{invoice_id}",
    response_model=InvoiceResponse,
)
def get_invoice(
    invoice_id: int,
    service: InvoiceService = Depends(
        get_invoice_service
    ),
):

    try:

        invoice = service.get_by_id(
            invoice_id
        )


        if invoice is None:

            raise HTTPException(
                status_code=404,
                detail="Invoice not found.",
            )


        return invoice


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ======================================
# CREATE INVOICE
# ======================================

@router.post(
    "/",
    response_model=InvoiceResponse,
)
def create_invoice(
    invoice: InvoiceCreate,
    service: InvoiceService = Depends(
        get_invoice_service
    ),
):

    try:

        return service.create(
            invoice.model_dump()
        )


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ======================================
# UPDATE INVOICE
# ======================================

@router.put(
    "/{invoice_id}",
    response_model=InvoiceResponse,
)
def update_invoice(
    invoice_id: int,
    invoice: InvoiceUpdate,
    service: InvoiceService = Depends(
        get_invoice_service
    ),
):

    try:

        updated_invoice = service.update(
            invoice_id,
            invoice.model_dump(
                exclude_unset=True
            ),
        )


        if updated_invoice is None:

            raise HTTPException(
                status_code=404,
                detail="Invoice not found.",
            )


        return updated_invoice


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ======================================
# DELETE INVOICE
# ======================================

@router.delete("/{invoice_id}")
def delete_invoice(
    invoice_id: int,
    service: InvoiceService = Depends(
        get_invoice_service
    ),
):

    try:

        deleted = service.delete(
            invoice_id
        )


        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Invoice not found.",
            )


        return {
            "message": "Invoice deleted successfully."
        }


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )