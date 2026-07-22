"""
Machine Service

Business Logic Layer

Build-012
"""

from app.repositories.machine_repository import (
    MachineRepository,
)

from app.schemas.machine import (
    MachineCreate,
    MachineUpdate,
)


class MachineService:

    def __init__(
        self,
        repository: MachineRepository,
    ):
        self.repository = repository

    def create(
        self,
        machine: MachineCreate,
    ):

        existing = self.repository.get_by_code(
            machine.machine_code
        )

        if existing:
            raise ValueError(
                "Machine Code already exists."
            )

        return self.repository.create(
            machine
        )

    def get_all(self):

        return self.repository.get_all()

    def get_active(self):

        return self.repository.get_active()

    def get_by_id(
        self,
        machine_id: int,
    ):

        db_machine = self.repository.get_by_id(
            machine_id
        )

        if not db_machine:
            raise ValueError(
                "Machine not found."
            )

        return db_machine

    def update(
        self,
        machine_id: int,
        machine: MachineUpdate,
    ):

        db_machine = self.repository.get_by_id(
            machine_id
        )

        if not db_machine:
            raise ValueError(
                "Machine not found."
            )

        return self.repository.update(
            db_machine,
            machine,
        )

    def delete(
        self,
        machine_id: int,
    ):

        db_machine = self.repository.get_by_id(
            machine_id
        )

        if not db_machine:
            raise ValueError(
                "Machine not found."
            )

        self.repository.delete(
            db_machine
        )

    def search(
        self,
        keyword: str,
    ):

        return self.repository.search(
            keyword
        )