from sqlalchemy.orm import Session

from app.models.binding_type import BindingType
from app.repositories.binding_type_repository import BindingTypeRepository
from app.schemas.binding_type import (
    BindingTypeCreate,
    BindingTypeUpdate,
)


class BindingTypeService:

    def __init__(self):
        self.repository = BindingTypeRepository()

    def create(self, db: Session, data: BindingTypeCreate):

        existing = self.repository.get_by_code(
            db,
            data.binding_type_code
        )

        if existing:
            raise ValueError("Binding Type Code already exists.")

        obj = BindingType(**data.model_dump())

        return self.repository.create(db, obj)

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, binding_type_id: int):

        obj = self.repository.get_by_id(
            db,
            binding_type_id
        )

        if not obj:
            raise ValueError("Binding Type not found.")

        return obj

    def update(
        self,
        db: Session,
        binding_type_id: int,
        data: BindingTypeUpdate,
    ):

        obj = self.repository.get_by_id(
            db,
            binding_type_id
        )

        if not obj:
            raise ValueError("Binding Type not found.")

        update_data = data.model_dump()

        for key, value in update_data.items():
            setattr(obj, key, value)

        return self.repository.update(db, obj)

    def delete(
        self,
        db: Session,
        binding_type_id: int,
    ):

        obj = self.repository.get_by_id(
            db,
            binding_type_id
        )

        if not obj:
            raise ValueError("Binding Type not found.")

        self.repository.delete(db, obj)

        return {
            "message": "Binding Type deleted successfully."
        }