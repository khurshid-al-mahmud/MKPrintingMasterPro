"""
MKPrintingMasterPro ERP

Job Order API

Build-030
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repositories.job_order_repository import (
    JobOrderRepository,
)

from app.repositories.invoice_repository import (
    InvoiceRepository,
)

from app.services.numbering import (
    NumberingService,
)

from app.services.job_order_service import (
    JobOrderService,
)

from app.schemas.job_order import (
    JobOrderResponse,
)


router = APIRouter(
    prefix="/job-order",
    tags=["Job Order"],
)



# =====================================
# Create Job Order From Invoice
# =====================================

@router.post(
    "/from-invoice/{invoice_id}",
    response_model=JobOrderResponse,
)
def create_job_order(
    invoice_id: int,
    db: Session = Depends(get_db),
):

    job_order_repository = JobOrderRepository(db)

    invoice_repository = InvoiceRepository(db)

    numbering_service = NumberingService(db)


    service = JobOrderService(
        job_order_repository=job_order_repository,
        invoice_repository=invoice_repository,
        numbering_service=numbering_service,
        db=db,
    )


    try:

        return service.create_from_invoice(
            invoice_id
        )


    except ValueError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex),
        )





# =====================================
# Get Job Order By ID
# =====================================

@router.get(
    "/{job_order_id}",
    response_model=JobOrderResponse,
)
def get_job_order(
    job_order_id: int,
    db: Session = Depends(get_db),
):

    repository = JobOrderRepository(db)


    job_order = repository.get_by_id(
        job_order_id
    )


    if job_order is None:

        raise HTTPException(
            status_code=404,
            detail="Job Order not found.",
        )


    return job_order





# =====================================
# Get All Job Orders
# =====================================

@router.get(
    "",
    response_model=list[JobOrderResponse],
)
def get_job_orders(
    db: Session = Depends(get_db),
):

    repository = JobOrderRepository(db)


    return repository.get_all()





# =====================================
# Update Job Order Status
# Build-030 Phase-6 Step-3
# =====================================

@router.put(
    "/{job_order_id}/status",
    response_model=JobOrderResponse,
)
def update_job_order_status(
    job_order_id: int,
    status: str,
    db: Session = Depends(get_db),
):


    job_order_repository = JobOrderRepository(db)


    invoice_repository = InvoiceRepository(db)


    numbering_service = NumberingService(db)



    service = JobOrderService(

        job_order_repository=job_order_repository,

        invoice_repository=invoice_repository,

        numbering_service=numbering_service,

        db=db,

    )



    try:

        return service.update_status(

            job_order_id,

            status,

            changed_by="Admin",

        )


    except ValueError as ex:

        raise HTTPException(

            status_code=404,

            detail=str(ex),

        )