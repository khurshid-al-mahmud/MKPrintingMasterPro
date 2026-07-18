"""
Machine Service.

Business Logic Layer
for Machine Management.
"""

from app.models.machine import Machine
from app.repositories.machine_repository import MachineRepository
from app.schemas.machine import (
    MachineCreate,
    MachineUpdate,
)


class MachineService:
    """
    Service layer for Machine management.
    """

    def __init__(
        self,
        repository: MachineRepository,
    ) -> None:
        self.repository = repository

    def create(
        self,
        machine: MachineCreate,
    ) -> Machine:
        """
        Create machine.
        """

        if self.repository.exists_by_machine_code(
            machine.machine_code,
        ):
            raise ValueError(
                "Machine Code already exists.",
            )

        if self.repository.exists_by_machine_name(
            machine.machine_name,
        ):
            raise ValueError(
                "Machine Name already exists.",
            )

        new_machine = Machine(
            machine_code=machine.machine_code,
            machine_name=machine.machine_name,
            machine_type=machine.machine_type,
            manufacturer=machine.manufacturer,
            model=machine.model,
            max_sheet_size=machine.max_sheet_size,
            max_print_width=machine.max_print_width,
            max_print_length=machine.max_print_length,
            color_capacity=machine.color_capacity,
            production_speed=machine.production_speed,
            hourly_running_cost=machine.hourly_running_cost,
            remarks=machine.remarks,
        )

        return self.repository.create(
            new_machine,
        )

    def get_by_id(
        self,
        machine_id: int,
    ) -> Machine | None:
        """
        Get machine by ID.
        """

        return self.repository.get_by_id(
            machine_id,
        )

    def get_all(
        self,
    ) -> list[Machine]:
        """
        Get all machines.
        """

        return self.repository.get_all()

    def update(
        self,
        machine_id: int,
        machine_data: MachineUpdate,
    ) -> Machine | None:
        """
        Update machine.
        """

        return self.repository.update(
            machine_id,
            machine_data.model_dump(
                exclude_unset=True,
            ),
        )

    def delete(
        self,
        machine_id: int,
    ) -> bool:
        """
        Soft delete machine.
        """

        return self.repository.soft_delete(
            machine_id,
        )

    def search(
        self,
        keyword: str,
    ) -> list[Machine]:
        """
        Search machines.
        """

        return self.repository.search(
            keyword,
        )