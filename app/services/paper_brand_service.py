"""
Paper Brand Service.

Contains all business logic
for Paper Brand Master.
"""

from app.repositories.paper_brand_repository import PaperBrandRepository
from app.schemas.paper_brand import PaperBrandCreate
from app.schemas.paper_brand import PaperBrandUpdate


class PaperBrandService:
    """Paper Brand Service."""

    def __init__(self, repository: PaperBrandRepository):
        self.repository = repository

    def create(self, paper_brand: PaperBrandCreate):
        """Create Paper Brand."""

        existing_code = self.repository.get_by_code(
            paper_brand.paper_brand_code
        )

        if existing_code:
            raise ValueError(
                "Paper Brand Code already exists."
            )

        existing_name = self.repository.get_by_name(
            paper_brand.paper_brand_name
        )

        if existing_name:
            raise ValueError(
                "Paper Brand Name already exists."
            )

        return self.repository.create(paper_brand)

    def get_all(self):
        """Get all Paper Brands."""

        return self.repository.get_all()

    def get_active(self):
        """Get active Paper Brands."""

        return self.repository.get_active()

    def get_by_id(self, paper_brand_id: int):
        """Get Paper Brand by ID."""

        paper_brand = self.repository.get_by_id(
            paper_brand_id
        )

        if not paper_brand:
            raise ValueError(
                "Paper Brand not found."
            )

        return paper_brand

    def update(
        self,
        paper_brand_id: int,
        paper_brand: PaperBrandUpdate,
    ):
        """Update Paper Brand."""

        db_paper_brand = self.repository.get_by_id(
            paper_brand_id
        )

        if not db_paper_brand:
            raise ValueError(
                "Paper Brand not found."
            )

        if (
            paper_brand.paper_brand_code
            and paper_brand.paper_brand_code
            != db_paper_brand.paper_brand_code
        ):
            existing_code = self.repository.get_by_code(
                paper_brand.paper_brand_code
            )

            if existing_code:
                raise ValueError(
                    "Paper Brand Code already exists."
                )

        if (
            paper_brand.paper_brand_name
            and paper_brand.paper_brand_name
            != db_paper_brand.paper_brand_name
        ):
            existing_name = self.repository.get_by_name(
                paper_brand.paper_brand_name
            )

            if existing_name:
                raise ValueError(
                    "Paper Brand Name already exists."
                )

        return self.repository.update(
            db_paper_brand,
            paper_brand,
        )

    def delete(self, paper_brand_id: int):
        """Delete Paper Brand."""

        db_paper_brand = self.repository.get_by_id(
            paper_brand_id
        )

        if not db_paper_brand:
            raise ValueError(
                "Paper Brand not found."
            )

        self.repository.delete(db_paper_brand)

    def search(self, keyword: str):
        """Search Paper Brands."""

        return self.repository.search(keyword)