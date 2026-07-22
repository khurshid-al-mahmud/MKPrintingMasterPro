"""
Machine API

Build-012
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db

from app.repositories.machine_repository import (
    MachineRepository,
)

from app.schemas.machine import (
    MachineCreate,
    MachineResponse,
    MachineUpdate,
)

from app.services.machine_service import (
    MachineService,
)

router = APIRouter(
    prefix="/machines",
    tags=["Machine"],
)


def get_machine_service(
    db: Session = Depends(get_db),
):

    repository = MachineRepository(db)

    return MachineService(repository)


@router.post(
    "/",
    response_model=MachineResponse,
)
def create_machine(
    machine: MachineCreate,
    service: MachineService = Depends(
        get_machine_service
    ),
):

    try:
        return service.create(machine)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/",
    response_model=list[MachineResponse],
)
def get_all_machines(
    service: MachineService = Depends(
        get_machine_service
    ),
):

    return service.get_all()


@router.get(
    "/active",
    response_model=list[MachineResponse],
)
def get_active_machines(
    service: MachineService = Depends(
        get_machine_service
    ),
):

    return service.get_active()


@router.get(
    "/{machine_id}",
    response_model=MachineResponse,
)
def get_machine(
    machine_id: int,
    service: MachineService = Depends(
        get_machine_service
    ),
):

    try:
        return service.get_by_id(machine_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.put(
    "/{machine_id}",
    response_model=MachineResponse,
)
def update_machine(
    machine_id: int,
    machine: MachineUpdate,
    service: MachineService = Depends(
        get_machine_service
    ),
):

    try:
        return service.update(
            machine_id,
            machine,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete(
    "/{machine_id}",
)
def delete_machine(
    machine_id: int,
    service: MachineService = Depends(
        get_machine_service
    ),
):

    try:
        service.delete(machine_id)

        return {
            "message": "Machine deleted successfully."
        }

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.get(
    "/search/{keyword}",
    response_model=list[MachineResponse],
)
def search_machine(
    keyword: str,
    service: MachineService = Depends(
        get_machine_service
    ),
):

    return service.search(keyword)