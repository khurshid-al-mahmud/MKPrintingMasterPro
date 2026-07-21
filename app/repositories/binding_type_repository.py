from sqlalchemy.orm import Session

from app.models.binding_type import BindingType


class BindingTypeRepository:

    def create(self, db: Session, obj: BindingType):
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get_all(self, db: Session):
        return (
            db.query(BindingType)
            .order_by(
                BindingType.display_order,
                BindingType.id
            )
            .all()
        )

    def get_by_id(self, db: Session, binding_type_id: int):
        return (
            db.query(BindingType)
            .filter(
                BindingType.id == binding_type_id
            )
            .first()
        )

    def get_by_code(self, db: Session, code: str):
        return (
            db.query(BindingType)
            .filter(
                BindingType.binding_type_code == code
            )
            .first()
        )

    def update(self, db: Session, obj: BindingType):
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, obj: BindingType):
        db.delete(obj)
        db.commit()