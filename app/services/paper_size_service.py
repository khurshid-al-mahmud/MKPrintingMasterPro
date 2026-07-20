"""
Paper Size Service.

Business logic for
Paper Size Master.
"""

from app.models.paper_size import PaperSize
from app.repositories.paper_size_repository import PaperSizeRepository
from app.schemas.paper_size import PaperSizeCreate
from app.schemas.paper_size import PaperSizeUpdate


class PaperSizeService:
    """Service for Paper Size."""

    def __init__(
        self,
        repository: PaperSizeRepository,
    ):
        self.repository = repository

    def create(
        self,
        data: PaperSizeCreate,
    ) -> PaperSize:
        """Create Paper Size."""

        paper_size = PaperSize(
            paper_size_code=data.paper_size_code,
            paper_size_name=data.paper_size_name,
            width_mm=data.width_mm,
            height_mm=data.height_mm,
            display_order=data.display_order,
            is_active=data.is_active,
        )

        return self.repository.create(
            paper_size,
        )

    def get_by_id(
        self,
        paper_size_id: int,
    ) -> PaperSize | None:
        """Get Paper Size by ID."""

        return self.repository.get_by_id(
            paper_size_id,
        )

    def get_all(
        self,
    ) -> list[PaperSize]:
        """Get all Paper Sizes."""

        return self.repository.get_all()

    def update(
        self,
        paper_size_id: int,
        data: PaperSizeUpdate,
    ) -> PaperSize | None:
        """Update Paper Size."""

        paper_size = self.repository.get_by_id(
            paper_size_id,
        )

        if not paper_size:
            return None

        update_data = data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                paper_size,
                field,
                value,
            )

        return self.repository.update(
            paper_size,
        )

    def delete(
        self,
        paper_size_id: int,
    ) -> bool:
        """Delete Paper Size."""

        paper_size = self.repository.get_by_id(
            paper_size_id,
        )

        if not paper_size:
            return False

        self.repository.delete(
            paper_size,
        )

        return True