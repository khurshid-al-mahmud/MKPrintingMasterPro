"""
Customer API.

REST API endpoints
for Customer Management.
"""

from fastapi import APIRouter, Depends

from app.api.dependencies.service import get_customer_service
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse,
    CustomerUpdate,
)
from app.services.customer_service import CustomerService

router = APIRouter(
    prefix="/customer",
    tags=["Customer"],
)


@router.get(
    "/",
    response_model=list[CustomerResponse],
)
def get_all_customers(
    service: CustomerService = Depends(
        get_customer_service,
    ),
):
    """
    Get all customers.
    """

    return service.get_all()


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def get_customer(
    customer_id: int,
    service: CustomerService = Depends(
        get_customer_service,
    ),
):
    """
    Get customer by ID.
    """

    return service.get_by_id(
        customer_id,
    )


@router.post(
    "/",
    response_model=CustomerResponse,
)
def create_customer(
    customer: CustomerCreate,
    service: CustomerService = Depends(
        get_customer_service,
    ),
):
    """
    Create customer.
    """

    return service.create(
        customer,
    )


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse,
)
def update_customer(
    customer_id: int,
    customer: CustomerUpdate,
    service: CustomerService = Depends(
        get_customer_service,
    ),
):
    """
    Update customer.
    """

    return service.update(
        customer_id,
        customer,
    )


@router.delete(
    "/{customer_id}",
)
def delete_customer(
    customer_id: int,
    service: CustomerService = Depends(
        get_customer_service,
    ),
):
    """
    Soft delete customer.
    """

    return service.delete(
        customer_id,
    )


@router.get(
    "/search/{keyword}",
    response_model=list[CustomerResponse],
)
def search_customer(
    keyword: str,
    service: CustomerService = Depends(
        get_customer_service,
    ),
):
    """
    Search customers.
    """

    return service.search(
        keyword,
    )