"""
Paper GSM API.

REST API for Paper GSM Master.
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.api.dependencies.service import get_paper_gsm_service
from app.schemas.paper_gsm import PaperGSMCreate
from app.schemas.paper_gsm import PaperGSMResponse
from app.schemas.paper_gsm import PaperGSMUpdate
from app.services.paper_gsm_service import PaperGSMService

router = APIRouter(
    prefix="/paper-gsm",
    tags=["Paper GSM"],
)


@router.get(
    "/",
    response_model=list[PaperGSMResponse],
)
def get_all_paper_gsms(
    service: PaperGSMService = Depends(get_paper_gsm_service),
):
    """Get all Paper GSM."""
    return service.get_all()


@router.get(
    "/active",
    response_model=list[PaperGSMResponse],
)
def get_active_paper_gsms(
    service: PaperGSMService = Depends(get_paper_gsm_service),
):
    """Get active Paper GSM."""
    return service.get_active()


@router.get(
    "/{paper_gsm_id}",
    response_model=PaperGSMResponse,
)
def get_paper_gsm(
    paper_gsm_id: int,
    service: PaperGSMService = Depends(get_paper_gsm_service),
):
    """Get Paper GSM."""
    try:
        return service.get_by_id(paper_gsm_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.post(
    "/",
    response_model=PaperGSMResponse,
)
def create_paper_gsm(
    paper_gsm: PaperGSMCreate,
    service: PaperGSMService = Depends(get_paper_gsm_service),
):
    """Create Paper GSM."""
    try:
        return service.create(paper_gsm)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.put(
    "/{paper_gsm_id}",
    response_model=PaperGSMResponse,
)
def update_paper_gsm(
    paper_gsm_id: int,
    paper_gsm: PaperGSMUpdate,
    service: PaperGSMService = Depends(get_paper_gsm_service),
):
    """Update Paper GSM."""
    try:
        return service.update(
            paper_gsm_id,
            paper_gsm,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.delete(
    "/{paper_gsm_id}",
)
def delete_paper_gsm(
    paper_gsm_id: int,
    service: PaperGSMService = Depends(get_paper_gsm_service),
):
    """Delete Paper GSM."""
    try:
        service.delete(paper_gsm_id)
        return {
            "message": "Paper GSM deleted successfully."
        }
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.get(
    "/search/{keyword}",
    response_model=list[PaperGSMResponse],
)
def search_paper_gsms(
    keyword: str,
    service: PaperGSMService = Depends(get_paper_gsm_service),
):
    """Search Paper GSM."""
    return service.search(keyword)