"""
Quotation API.

REST API endpoints
for Quotation Management.
"""

import traceback

from fastapi import APIRouter, Depends, HTTPException

from app.api.dependencies.service import get_quotation_service

from app.schemas.quotation import (
    QuotationCreate,
    QuotationResponse,
    QuotationUpdate,
)

from app.services.quotation_service import QuotationService


router = APIRouter(
    prefix="/quotation",
    tags=["Quotation"],
)


# ======================================
# GET ALL QUOTATIONS
# ======================================

@router.get(
    "/",
    response_model=list[QuotationResponse],
)
def get_all_quotations(
    service: QuotationService = Depends(get_quotation_service),
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
# GET SINGLE QUOTATION
# ======================================

@router.get(
    "/{quotation_id}",
    response_model=QuotationResponse,
)
def get_quotation(
    quotation_id: int,
    service: QuotationService = Depends(get_quotation_service),
):
    try:

        quotation = service.get_by_id(
            quotation_id
        )


        if quotation is None:

            raise HTTPException(
                status_code=404,
                detail="Quotation not found.",
            )


        return quotation


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ======================================
# CREATE QUOTATION
# ======================================

@router.post(
    "/",
    response_model=QuotationResponse,
)
def create_quotation(
    quotation: QuotationCreate,
    service: QuotationService = Depends(get_quotation_service),
):
    try:

        return service.create(
            quotation
        )


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ======================================
# UPDATE QUOTATION
# ======================================

@router.put(
    "/{quotation_id}",
    response_model=QuotationResponse,
)
def update_quotation(
    quotation_id: int,
    quotation: QuotationUpdate,
    service: QuotationService = Depends(get_quotation_service),
):
    try:

        updated_quotation = service.update(
            quotation_id,
            quotation,
        )


        if updated_quotation is None:

            raise HTTPException(
                status_code=404,
                detail="Quotation not found.",
            )


        return updated_quotation


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )



# ======================================
# DELETE QUOTATION
# ======================================

@router.delete(
    "/{quotation_id}",
)
def delete_quotation(
    quotation_id: int,
    service: QuotationService = Depends(get_quotation_service),
):
    try:

        deleted = service.delete(
            quotation_id
        )


        if not deleted:

            raise HTTPException(
                status_code=404,
                detail="Quotation not found.",
            )


        return {
            "message": "Quotation deleted successfully."
        }


    except HTTPException:

        raise


    except Exception as e:

        print(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )