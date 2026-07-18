"""
Machine API.

REST API endpoints
for Machine Management.
"""

from fastapi import APIRouter, Depends

from app.api.dependencies.service import get_machine_service
from app.schemas.machine import (
    MachineCreate,
    MachineResponse,
    MachineUpdate,
)
from app.services.machine_service import MachineService

router = APIRouter(
    prefix="/machine",
    tags=["Machine"],
)


@router.get(
    "/",
    response_model=list[MachineResponse],
)
def get_all_machines(
    service: MachineService = Depends(
        get_machine_service,
    ),
):
    """
    Get all machines.
    """

    return service.get_all()


@router.get(
    "/{machine_id}",
    response_model=MachineResponse,
)
def get_machine(
    machine_id: int,
    service: MachineService = Depends(
        get_machine_service,
    ),
):
    """
    Get machine by ID.
    """

    return service.get_by_id(
        machine_id,
    )


@router.post(
    "/",
    response_model=MachineResponse,
)
def create_machine(
    machine: MachineCreate,
    service: MachineService = Depends(
        get_machine_service,
    ),
):
    """
    Create machine.
    """

    return service.create(
        machine,
    )


@router.put(
    "/{machine_id}",
    response_model=MachineResponse,
)
def update_machine(
    machine_id: int,
    machine: MachineUpdate,
    service: MachineService = Depends(
        get_machine_service,
    ),
):
    """
    Update machine.
    """

    return service.update(
        machine_id,
        machine,
    )


@router.delete(
    "/{machine_id}",
)
def delete_machine(
    machine_id: int,
    service: MachineService = Depends(
        get_machine_service,
    ),
):
    """
    Soft delete machine.
    """

    return service.delete(
        machine_id,
    )


@router.get(
    "/search/{keyword}",
    response_model=list[MachineResponse],
)
def search_machine(
    keyword: str,
    service: MachineService = Depends(
        get_machine_service,
    ),
):
    """
    Search machines.
    """

    return service.search(
        keyword,
    )