"""
Paper Type Service.

Contains all business logic
for Paper Type Master.
"""

from app.repositories.paper_type_repository import PaperTypeRepository
from app.schemas.paper_type import PaperTypeCreate
from app.schemas.paper_type import PaperTypeUpdate


class PaperTypeService:
    """Paper Type Service."""

    def __init__(self, repository: PaperTypeRepository):
        self.repository = repository

    def create(self, paper_type: PaperTypeCreate):
        """Create Paper Type."""

        existing_code = self.repository.get_by_code(
            paper_type.paper_type_code
        )

        if existing_code:
            raise ValueError("Paper Type Code already exists.")

        existing_name = self.repository.get_by_name(
            paper_type.paper_type_name
        )

        if existing_name:
            raise ValueError("Paper Type Name already exists.")

        return self.repository.create(paper_type)

    def get_all(self):
        """Get all Paper Types."""

        return self.repository.get_all()

    def get_active(self):
        """Get active Paper Types."""

        return self.repository.get_active()

    def get_by_id(self, paper_type_id: int):
        """Get Paper Type by ID."""

        paper_type = self.repository.get_by_id(paper_type_id)

        if not paper_type:
            raise ValueError("Paper Type not found.")

        return paper_type

    def update(
        self,
        paper_type_id: int,
        paper_type: PaperTypeUpdate,
    ):
        """Update Paper Type."""

        db_paper_type = self.repository.get_by_id(
            paper_type_id
        )

        if not db_paper_type:
            raise ValueError("Paper Type not found.")

        if (
            paper_type.paper_type_code
            and paper_type.paper_type_code
            != db_paper_type.paper_type_code
        ):
            existing_code = self.repository.get_by_code(
                paper_type.paper_type_code
            )

            if existing_code:
                raise ValueError(
                    "Paper Type Code already exists."
                )

        if (
            paper_type.paper_type_name
            and paper_type.paper_type_name
            != db_paper_type.paper_type_name
        ):
            existing_name = self.repository.get_by_name(
                paper_type.paper_type_name
            )

            if existing_name:
                raise ValueError(
                    "Paper Type Name already exists."
                )

        return self.repository.update(
            db_paper_type,
            paper_type,
        )

    def delete(self, paper_type_id: int):
        """Delete Paper Type."""

        db_paper_type = self.repository.get_by_id(
            paper_type_id
        )

        if not db_paper_type:
            raise ValueError("Paper Type not found.")

        self.repository.delete(db_paper_type)

    def search(self, keyword: str):
        """Search Paper Types."""

        return self.repository.search(keyword)