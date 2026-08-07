"""
MKPrintingMasterPro ERP

Specification Runtime API

Phase-8
Dynamic Runtime Engine
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.specification_runtime_service import (
    SpecificationRuntimeService,
)

router = APIRouter(
    prefix="/specification-runtime",
    tags=["Specification Runtime"],
)


@router.get("/template/{template_id}")
def get_template_runtime(
    template_id: int,
    db: Session = Depends(get_db),
):
    """
    Get Runtime Template Structure
    """
    service = SpecificationRuntimeService(db)

    return service.get_template_runtime(
        template_id
    )