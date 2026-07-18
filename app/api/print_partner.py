"""
Print Partner API.

REST API endpoints
for Print Partner Management.
"""

from fastapi import APIRouter, Depends

from app.api.dependencies.service import (
    get_print_partner_service,
)
from app.schemas.print_partner import (
    PrintPartnerCreate,
    PrintPartnerResponse,
    PrintPartnerUpdate,
)
from app.services.print_partner_service import (
    PrintPartnerService,
)


router = APIRouter(
    prefix="/print-partner",
    tags=["Print Partner"],
)


@router.get(
    "/",
    response_model=list[PrintPartnerResponse],
)
def get_all_print_partners(
    service: PrintPartnerService = Depends(
        get_print_partner_service,
    ),
):
    """
    Get all print partners.
    """

    return service.get_all()



@router.get(
    "/{partner_id}",
    response_model=PrintPartnerResponse,
)
def get_print_partner(
    partner_id: int,
    service: PrintPartnerService = Depends(
        get_print_partner_service,
    ),
):
    """
    Get print partner by ID.
    """

    return service.get_by_id(
        partner_id,
    )



@router.post(
    "/",
    response_model=PrintPartnerResponse,
)
def create_print_partner(
    partner: PrintPartnerCreate,
    service: PrintPartnerService = Depends(
        get_print_partner_service,
    ),
):
    """
    Create print partner.
    """

    return service.create(
        partner,
    )



@router.put(
    "/{partner_id}",
    response_model=PrintPartnerResponse,
)
def update_print_partner(
    partner_id: int,
    partner: PrintPartnerUpdate,
    service: PrintPartnerService = Depends(
        get_print_partner_service,
    ),
):
    """
    Update print partner.
    """

    return service.update(
        partner_id,
        partner,
    )



@router.delete(
    "/{partner_id}",
)
def delete_print_partner(
    partner_id: int,
    service: PrintPartnerService = Depends(
        get_print_partner_service,
    ),
):
    """
    Soft delete print partner.
    """

    return service.delete(
        partner_id,
    )



@router.get(
    "/search/{keyword}",
    response_model=list[PrintPartnerResponse],
)
def search_print_partner(
    keyword: str,
    service: PrintPartnerService = Depends(
        get_print_partner_service,
    ),
):
    """
    Search print partners.
    """

    return service.search(
        keyword,
    )