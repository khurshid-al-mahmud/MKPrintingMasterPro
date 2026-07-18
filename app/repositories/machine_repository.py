"""
Machine Repository.

Database access layer
for Machine Management.
"""

from sqlalchemy import or_

from app.models.machine import Machine


class MachineRepository:
    """
    Repository for Machine.
    """

    def __init__(
        self,
        db,
    ):
        self.db = db

    def create(
        self,
        machine: Machine,
    ) -> Machine:

        self.db.add(
            machine,
        )

        self.db.commit()

        self.db.refresh(
            machine,
        )

        return machine

    def get_by_id(
        self,
        machine_id: int,
    ) -> Machine | None:

        return (
            self.db.query(
                Machine,
            )
            .filter(
                Machine.id == machine_id,
                Machine.is_active == True,
            )
            .first()
        )

    def get_all(
        self,
    ) -> list[Machine]:

        return (
            self.db.query(
                Machine,
            )
            .filter(
                Machine.is_active == True,
            )
            .all()
        )

    def update(
        self,
        machine_id: int,
        machine_data: dict,
    ) -> Machine | None:

        machine = self.get_by_id(
            machine_id,
        )

        if machine is None:
            return None

        for key, value in machine_data.items():
            setattr(
                machine,
                key,
                value,
            )

        self.db.commit()

        self.db.refresh(
            machine,
        )

        return machine

    def soft_delete(
        self,
        machine_id: int,
    ) -> bool:

        machine = self.get_by_id(
            machine_id,
        )

        if machine is None:
            return False

        machine.is_active = False

        self.db.commit()

        return True

    def search(
        self,
        keyword: str,
    ) -> list[Machine]:

        return (
            self.db.query(
                Machine,
            )
            .filter(
                Machine.is_active == True,
            )
            .filter(
                or_(
                    Machine.machine_name.ilike(
                        f"%{keyword}%",
                    ),
                    Machine.machine_code.ilike(
                        f"%{keyword}%",
                    ),
                    Machine.machine_type.ilike(
                        f"%{keyword}%",
                    ),
                    Machine.manufacturer.ilike(
                        f"%{keyword}%",
                    ),
                )
            )
            .all()
        )

    def exists_by_machine_code(
        self,
        machine_code: str,
    ) -> bool:

        return (
            self.db.query(
                Machine,
            )
            .filter(
                Machine.machine_code == machine_code,
                Machine.is_active == True,
            )
            .first()
            is not None
        )

    def exists_by_machine_name(
        self,
        machine_name: str,
    ) -> bool:

        return (
            self.db.query(
                Machine,
            )
            .filter(
                Machine.machine_name == machine_name,
                Machine.is_active == True,
            )
            .first()
            is not None
        )