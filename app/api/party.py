"""
Party API.

REST API endpoints
for Party Management.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.api.dependencies.service import get_party_service
from app.schemas.party import (
    PartyCreate,
    PartyResponse,
    PartyUpdate,
)
from app.services.party_service import PartyService

router = APIRouter(
    prefix="/party",
    tags=["Party"],
)


@router.get(
    "/",
    response_model=list[PartyResponse],
)
def get_all_parties(
    service: PartyService = Depends(get_party_service),
):
    """
    Get all active parties.
    """
    return service.get_all()


@router.get(
    "/{party_id}",
    response_model=PartyResponse,
)
def get_party(
    party_id: int,
    service: PartyService = Depends(get_party_service),
):
    """
    Get party by ID.
    """
    return service.get_by_id(
        party_id,
    )


@router.post(
    "/",
    response_model=PartyResponse,
)
def create_party(
    party: PartyCreate,
    service: PartyService = Depends(get_party_service),
):
    """
    Create new party.
    """
    return service.create(
        party,
    )


@router.put(
    "/{party_id}",
    response_model=PartyResponse,
)
def update_party(
    party_id: int,
    party: PartyUpdate,
    service: PartyService = Depends(get_party_service),
):
    """
    Update existing party.
    """
    return service.update(
        party_id,
        party,
    )


@router.delete(
    "/{party_id}",
)
def delete_party(
    party_id: int,
    service: PartyService = Depends(get_party_service),
):
    """
    Soft delete party.
    """
    return service.delete(
        party_id,
    )


@router.get(
    "/search/{keyword}",
    response_model=list[PartyResponse],
)
def search_party(
    keyword: str,
    service: PartyService = Depends(get_party_service),
):
    """
    Search parties.
    """
    return service.search(
        keyword,
    )