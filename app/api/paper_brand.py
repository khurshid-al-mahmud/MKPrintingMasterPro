"""
Paper Brand API.

REST API for Paper Brand Master.
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from app.api.dependencies.service import get_paper_brand_service
from app.schemas.paper_brand import PaperBrandCreate
from app.schemas.paper_brand import PaperBrandResponse
from app.schemas.paper_brand import PaperBrandUpdate
from app.services.paper_brand_service import PaperBrandService

router = APIRouter(
    prefix="/paper-brand",
    tags=["Paper Brand"],
)


@router.get(
    "/",
    response_model=list[PaperBrandResponse],
)
def get_all_paper_brands(
    service: PaperBrandService = Depends(get_paper_brand_service),
):
    """Get all Paper Brands."""
    return service.get_all()


@router.get(
    "/active",
    response_model=list[PaperBrandResponse],
)
def get_active_paper_brands(
    service: PaperBrandService = Depends(get_paper_brand_service),
):
    """Get active Paper Brands."""
    return service.get_active()


@router.get(
    "/{paper_brand_id}",
    response_model=PaperBrandResponse,
)
def get_paper_brand(
    paper_brand_id: int,
    service: PaperBrandService = Depends(get_paper_brand_service),
):
    """Get Paper Brand."""
    try:
        return service.get_by_id(paper_brand_id)
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.post(
    "/",
    response_model=PaperBrandResponse,
)
def create_paper_brand(
    paper_brand: PaperBrandCreate,
    service: PaperBrandService = Depends(get_paper_brand_service),
):
    """Create Paper Brand."""
    try:
        return service.create(paper_brand)
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.put(
    "/{paper_brand_id}",
    response_model=PaperBrandResponse,
)
def update_paper_brand(
    paper_brand_id: int,
    paper_brand: PaperBrandUpdate,
    service: PaperBrandService = Depends(get_paper_brand_service),
):
    """Update Paper Brand."""
    try:
        return service.update(
            paper_brand_id,
            paper_brand,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc


@router.delete(
    "/{paper_brand_id}",
)
def delete_paper_brand(
    paper_brand_id: int,
    service: PaperBrandService = Depends(get_paper_brand_service),
):
    """Delete Paper Brand."""
    try:
        service.delete(paper_brand_id)
        return {
            "message": "Paper Brand deleted successfully."
        }
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc


@router.get(
    "/search/{keyword}",
    response_model=list[PaperBrandResponse],
)
def search_paper_brands(
    keyword: str,
    service: PaperBrandService = Depends(get_paper_brand_service),
):
    """Search Paper Brands."""
    return service.search(keyword)