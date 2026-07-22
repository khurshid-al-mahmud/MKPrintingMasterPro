"""
Company Profile API.
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db

from app.models.company_profile import CompanyProfile

from app.repositories.company_profile_repository import (
    CompanyProfileRepository,
)

from app.schemas.company_profile import (
    CompanyProfileCreate,
    CompanyProfileResponse,
    CompanyProfileUpdate,
)

from app.services.company_profile_service import (
    CompanyProfileService,
)

router = APIRouter(
    prefix="/company-profile",
    tags=["Company Profile"],
)


def get_service(
    db: Session = Depends(get_db),
):
    repository = CompanyProfileRepository(db)
    return CompanyProfileService(repository)


@router.post(
    "/",
    response_model=CompanyProfileResponse,
)
def create_company_profile(
    company: CompanyProfileCreate,
    service: CompanyProfileService = Depends(get_service),
):
    return service.create(company)


@router.get(
    "/",
    response_model=CompanyProfileResponse | None,
)
def get_company_profile(
    service: CompanyProfileService = Depends(get_service),
):
    return service.get()


@router.get(
    "/{company_id}",
    response_model=CompanyProfileResponse,
)
def get_company_profile_by_id(
    company_id: int,
    service: CompanyProfileService = Depends(get_service),
):
    return service.get_by_id(company_id)


@router.put(
    "/{company_id}",
    response_model=CompanyProfileResponse,
)
def update_company_profile(
    company_id: int,
    company: CompanyProfileUpdate,
    service: CompanyProfileService = Depends(get_service),
):
    return service.update(
        company_id,
        company,
    )


@router.delete(
    "/{company_id}",
)
def delete_company_profile(
    company_id: int,
    service: CompanyProfileService = Depends(get_service),
):
    return service.delete(company_id)