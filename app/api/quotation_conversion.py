"""
MKPrintingMasterPro ERP

Quotation Conversion API

Build-029
Quotation -> Invoice Conversion
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repositories.quotation_repository import (
    QuotationRepository,
)

from app.repositories.invoice_repository import (
    InvoiceRepository,
)

from app.services.numbering import (
    NumberingService,
)

from app.services.quotation_conversion_service import (
    QuotationConversionService,
)

router = APIRouter(
    prefix="/quotation-conversion",
    tags=["Quotation Conversion"],
)


@router.post("/{quotation_id}")
def convert_quotation_to_invoice(
    quotation_id: int,
    db: Session = Depends(get_db),
):

    quotation_repository = QuotationRepository(db)

    invoice_repository = InvoiceRepository(db)

    numbering_service = NumberingService(db)

    service = QuotationConversionService(
        quotation_repository=quotation_repository,
        invoice_repository=invoice_repository,
        numbering_service=numbering_service,
    )

    try:

        invoice = service.convert(
            quotation_id
        )

        return {
            "success": True,
            "message": "Quotation converted successfully.",
            "invoice_id": invoice.id,
            "invoice_no": invoice.invoice_no,
            "quotation_status": "Converted",
        }

    except ValueError as ex:

        if str(ex) == "Quotation already converted.":

            raise HTTPException(
                status_code=409,
                detail=str(ex),
            )

        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex),
        )