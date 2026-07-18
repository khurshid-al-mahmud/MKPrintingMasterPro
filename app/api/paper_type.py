"""
Paper Type API.

REST API for Paper Type Master.
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.api.dependencies.service import get_paper_type_service
from app.schemas.paper_type import PaperTypeCreate
from app.schemas.paper_type import PaperTypeResponse
from app.schemas.paper_type import PaperTypeUpdate
from app.services.paper_type_service import PaperTypeService

router = APIRouter(
    prefix="/paper-type",
    tags=["Paper Type"],
)


@router.get(
    "/",
    response_model=list[PaperTypeResponse],
)
def get_all_paper_types(
    service: PaperTypeService = Depends(get_paper_type_service),
):
    """Get all Paper Types."""
    return service.get_all()


@router.get(
    "/active",
    response_model=list[PaperTypeResponse],
)
def get_active_paper_types(
    service: PaperTypeService = Depends(get_paper_type_service),
):
    """Get active Paper Types."""
    return service.get_active()


@router.get(
    "/{paper_type_id}",
    response_model=PaperTypeResponse,
)
def get_paper_type(
    paper_type_id: int,
    service: PaperTypeService = Depends(get_paper_type_service),
):
    """Get Paper Type."""
    try:
        return service.get_by_id(paper_type_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.post(
    "/",
    response_model=PaperTypeResponse,
)
def create_paper_type(
    paper_type: PaperTypeCreate,
    service: PaperTypeService = Depends(get_paper_type_service),
):
    """Create Paper Type."""
    try:
        return service.create(paper_type)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.put(
    "/{paper_type_id}",
    response_model=PaperTypeResponse,
)
def update_paper_type(
    paper_type_id: int,
    paper_type: PaperTypeUpdate,
    service: PaperTypeService = Depends(get_paper_type_service),
):
    """Update Paper Type."""
    try:
        return service.update(
            paper_type_id,
            paper_type,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.delete(
    "/{paper_type_id}",
)
def delete_paper_type(
    paper_type_id: int,
    service: PaperTypeService = Depends(get_paper_type_service),
):
    """Delete Paper Type."""
    try:
        service.delete(paper_type_id)
        return {
            "message": "Paper Type deleted successfully."
        }
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.get(
    "/search/{keyword}",
    response_model=list[PaperTypeResponse],
)
def search_paper_types(
    keyword: str,
    service: PaperTypeService = Depends(get_paper_type_service),
):
    """Search Paper Types."""
    return service.search(keyword)
