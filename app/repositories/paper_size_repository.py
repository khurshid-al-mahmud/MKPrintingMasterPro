"""
Paper Size Repository.

Handles all database operations
for Paper Size Master.
"""

from sqlalchemy.orm import Session

from app.models.paper_size import PaperSize


class PaperSizeRepository:
    """Repository for Paper Size."""

    def __init__(self, db: Session):
        self.db = db

    def create(self, paper_size: PaperSize) -> PaperSize:
        """Create Paper Size."""

        self.db.add(paper_size)
        self.db.commit()
        self.db.refresh(paper_size)

        return paper_size

    def get_by_id(
        self,
        paper_size_id: int,
    ) -> PaperSize | None:
        """Get Paper Size by ID."""

        return (
            self.db.query(PaperSize)
            .filter(
                PaperSize.id == paper_size_id,
            )
            .first()
        )

    def get_by_code(
        self,
        paper_size_code: str,
    ) -> PaperSize | None:
        """Get Paper Size by Code."""

        return (
            self.db.query(PaperSize)
            .filter(
                PaperSize.paper_size_code == paper_size_code,
            )
            .first()
        )

    def get_by_name(
        self,
        paper_size_name: str,
    ) -> PaperSize | None:
        """Get Paper Size by Name."""

        return (
            self.db.query(PaperSize)
            .filter(
                PaperSize.paper_size_name == paper_size_name,
            )
            .first()
        )

    def get_all(
        self,
    ) -> list[PaperSize]:
        """Get all Paper Sizes."""

        return (
            self.db.query(PaperSize)
            .order_by(
                PaperSize.display_order,
                PaperSize.paper_size_name,
            )
            .all()
        )

    def update(
        self,
        paper_size: PaperSize,
    ) -> PaperSize:
        """Update Paper Size."""

        self.db.commit()
        self.db.refresh(paper_size)

        return paper_size

    def delete(
        self,
        paper_size: PaperSize,
    ) -> None:
        """Delete Paper Size."""

        self.db.delete(paper_size)
        self.db.commit()