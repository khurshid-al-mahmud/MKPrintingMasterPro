"""
Paper Size API.

REST API endpoints
for Paper Size Master.
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.api.dependencies.service import get_paper_size_service
from app.schemas.paper_size import PaperSizeCreate
from app.schemas.paper_size import PaperSizeResponse
from app.schemas.paper_size import PaperSizeUpdate
from app.services.paper_size_service import PaperSizeService

router = APIRouter(
    prefix="/paper-sizes",
    tags=["Paper Size"],
)


@router.post(
    "/",
    response_model=PaperSizeResponse,
)
def create_paper_size(
    data: PaperSizeCreate,
    service: PaperSizeService = Depends(get_paper_size_service),
):
    """Create Paper Size."""

    return service.create(data)


@router.get(
    "/",
    response_model=list[PaperSizeResponse],
)
def get_all_paper_sizes(
    service: PaperSizeService = Depends(get_paper_size_service),
):
    """Get all Paper Sizes."""

    return service.get_all()


@router.get(
    "/{paper_size_id}",
    response_model=PaperSizeResponse,
)
def get_paper_size(
    paper_size_id: int,
    service: PaperSizeService = Depends(get_paper_size_service),
):
    """Get Paper Size by ID."""

    paper_size = service.get_by_id(
        paper_size_id,
    )

    if not paper_size:
        raise HTTPException(
            status_code=404,
            detail="Paper Size not found.",
        )

    return paper_size


@router.put(
    "/{paper_size_id}",
    response_model=PaperSizeResponse,
)
def update_paper_size(
    paper_size_id: int,
    data: PaperSizeUpdate,
    service: PaperSizeService = Depends(get_paper_size_service),
):
    """Update Paper Size."""

    paper_size = service.update(
        paper_size_id,
        data,
    )

    if not paper_size:
        raise HTTPException(
            status_code=404,
            detail="Paper Size not found.",
        )

    return paper_size


@router.delete(
    "/{paper_size_id}",
)
def delete_paper_size(
    paper_size_id: int,
    service: PaperSizeService = Depends(get_paper_size_service),
):
    """Delete Paper Size."""

    deleted = service.delete(
        paper_size_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Paper Size not found.",
        )

    return {
        "message": "Paper Size deleted successfully."
    }