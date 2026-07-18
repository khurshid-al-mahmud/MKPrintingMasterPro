"""
Paper Type Repository.

Handles all database operations
for Paper Type Master.
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.paper_type import PaperType
from app.schemas.paper_type import PaperTypeCreate
from app.schemas.paper_type import PaperTypeUpdate


class PaperTypeRepository:
    """Paper Type Repository."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, paper_type: PaperTypeCreate) -> PaperType:
        """Create new Paper Type."""

        db_paper_type = PaperType(**paper_type.model_dump())

        self.db.add(db_paper_type)
        self.db.commit()
        self.db.refresh(db_paper_type)

        return db_paper_type

    def get_all(self) -> list[PaperType]:
        """Get all Paper Types."""

        return (
            self.db.query(PaperType)
            .order_by(PaperType.display_order, PaperType.paper_type_name)
            .all()
        )

    def get_active(self) -> list[PaperType]:
        """Get active Paper Types."""

        return (
            self.db.query(PaperType)
            .filter(PaperType.is_active.is_(True))
            .order_by(PaperType.display_order, PaperType.paper_type_name)
            .all()
        )

    def get_by_id(self, paper_type_id: int) -> PaperType | None:
        """Get Paper Type by ID."""

        return (
            self.db.query(PaperType)
            .filter(PaperType.id == paper_type_id)
            .first()
        )

    def get_by_code(self, code: str) -> PaperType | None:
        """Get Paper Type by Code."""

        return (
            self.db.query(PaperType)
            .filter(PaperType.paper_type_code == code)
            .first()
        )

    def get_by_name(self, name: str) -> PaperType | None:
        """Get Paper Type by Name."""

        return (
            self.db.query(PaperType)
            .filter(PaperType.paper_type_name == name)
            .first()
        )

    def update(
        self,
        db_paper_type: PaperType,
        paper_type: PaperTypeUpdate,
    ) -> PaperType:
        """Update Paper Type."""

        update_data = paper_type.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_paper_type, key, value)

        self.db.commit()
        self.db.refresh(db_paper_type)

        return db_paper_type

    def delete(self, db_paper_type: PaperType) -> None:
        """Delete Paper Type."""

        self.db.delete(db_paper_type)
        self.db.commit()

    def search(self, keyword: str) -> list[PaperType]:
        """Search Paper Types."""

        return (
            self.db.query(PaperType)
            .filter(
                or_(
                    PaperType.paper_type_code.ilike(f"%{keyword}%"),
                    PaperType.paper_type_name.ilike(f"%{keyword}%"),
                )
            )
            .order_by(PaperType.display_order, PaperType.paper_type_name)
            .all()
        )