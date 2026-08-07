"""
MKPrintingMasterPro ERP

Job Order Status History API

Build-030 Phase-6 Step-3.4
"""


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database.session import get_db


from app.services.job_order_status_history_service import (
    JobOrderStatusHistoryService
)



router = APIRouter(
    prefix="/job-order",
    tags=[
        "Job Order Status History"
    ]
)



# ==========================================
# Get Job Order Status History
# ==========================================

@router.get(
    "/{job_order_id}/status-history"
)
def get_status_history(
    job_order_id: int,
    db: Session = Depends(get_db)
):

    service = JobOrderStatusHistoryService(
        db
    )


    history = (
        service.get_history_by_job_order(
            job_order_id
        )
    )


    if not history:

        raise HTTPException(
            status_code=404,
            detail="Job Order history not found."
        )


    return history