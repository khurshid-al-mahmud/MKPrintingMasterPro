"""
Employee API.

REST API endpoints
for Employee Management.
"""

from fastapi import APIRouter, Depends

from app.api.dependencies.service import get_employee_service
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
)
from app.services.employee_service import EmployeeService

router = APIRouter(
    prefix="/employee",
    tags=["Employee"],
)


@router.get(
    "/",
    response_model=list[EmployeeResponse],
)
def get_all_employees(
    service: EmployeeService = Depends(
        get_employee_service,
    ),
):
    """
    Get all employees.
    """

    return service.get_all()


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(
        get_employee_service,
    ),
):
    """
    Get employee by ID.
    """

    return service.get_by_id(
        employee_id,
    )


@router.post(
    "/",
    response_model=EmployeeResponse,
)
def create_employee(
    employee: EmployeeCreate,
    service: EmployeeService = Depends(
        get_employee_service,
    ),
):
    """
    Create employee.
    """

    return service.create(
        employee,
    )


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    service: EmployeeService = Depends(
        get_employee_service,
    ),
):
    """
    Update employee.
    """

    return service.update(
        employee_id,
        employee,
    )


@router.delete(
    "/{employee_id}",
)
def delete_employee(
    employee_id: int,
    service: EmployeeService = Depends(
        get_employee_service,
    ),
):
    """
    Soft delete employee.
    """

    return service.delete(
        employee_id,
    )


@router.get(
    "/search/{keyword}",
    response_model=list[EmployeeResponse],
)
def search_employee(
    keyword: str,
    service: EmployeeService = Depends(
        get_employee_service,
    ),
):
    """
    Search employees.
    """

    return service.search(
        keyword,
    )