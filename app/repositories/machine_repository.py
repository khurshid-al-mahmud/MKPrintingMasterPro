"""
Machine Repository

Build-012
"""

from sqlalchemy.orm import Session

from app.models.machine import Machine
from app.schemas.machine import (
    MachineCreate,
    MachineUpdate,
)


class MachineRepository:

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

    def create(
        self,
        machine: MachineCreate,
    ):

        db_machine = Machine(
            **machine.model_dump()
        )

        self.db.add(db_machine)
        self.db.commit()
        self.db.refresh(db_machine)

        return db_machine

    def get_all(self):

        return (
            self.db.query(Machine)
            .order_by(Machine.machine_name)
            .all()
        )

    def get_active(self):

        return (
            self.db.query(Machine)
            .filter(
                Machine.is_active.is_(True)
            )
            .order_by(Machine.machine_name)
            .all()
        )

    def get_by_id(
        self,
        machine_id: int,
    ):

        return (
            self.db.query(Machine)
            .filter(
                Machine.id == machine_id
            )
            .first()
        )

    def get_by_code(
        self,
        machine_code: str,
    ):

        return (
            self.db.query(Machine)
            .filter(
                Machine.machine_code == machine_code
            )
            .first()
        )

    def update(
        self,
        db_machine: Machine,
        machine: MachineUpdate,
    ):

        update_data = machine.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_machine,
                key,
                value,
            )

        self.db.commit()
        self.db.refresh(db_machine)

        return db_machine

    def delete(
        self,
        db_machine: Machine,
    ):

        self.db.delete(db_machine)
        self.db.commit()

    def search(
        self,
        keyword: str,
    ):

        return (
            self.db.query(Machine)
            .filter(
                Machine.machine_name.ilike(
                    f"%{keyword}%"
                )
            )
            .order_by(Machine.machine_name)
            .all()
        )