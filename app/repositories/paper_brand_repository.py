"""
Paper Brand Repository.

Database operations for
Paper Brand Master.
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.paper_brand import PaperBrand
from app.schemas.paper_brand import PaperBrandCreate
from app.schemas.paper_brand import PaperBrandUpdate


class PaperBrandRepository:
    """Paper Brand Repository."""

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        paper_brand: PaperBrandCreate,
    ) -> PaperBrand:
        """Create Paper Brand."""

        db_paper_brand = PaperBrand(
            **paper_brand.model_dump()
        )

        self.db.add(db_paper_brand)
        self.db.commit()
        self.db.refresh(db_paper_brand)

        return db_paper_brand

    def get_all(self) -> list[PaperBrand]:
        """Get all Paper Brands."""

        return (
            self.db.query(PaperBrand)
            .order_by(
                PaperBrand.display_order,
                PaperBrand.brand_name,
            )
            .all()
        )

    def get_active(self) -> list[PaperBrand]:
        """Get active Paper Brands."""

        return (
            self.db.query(PaperBrand)
            .filter(
                PaperBrand.is_active.is_(True)
            )
            .order_by(
                PaperBrand.display_order,
                PaperBrand.brand_name,
            )
            .all()
        )

    def get_by_id(
        self,
        paper_brand_id: int,
    ) -> PaperBrand | None:
        """Get Paper Brand by ID."""

        return (
            self.db.query(PaperBrand)
            .filter(
                PaperBrand.id == paper_brand_id
            )
            .first()
        )

    def get_by_code(
        self,
        brand_code: str,
    ) -> PaperBrand | None:
        """Get Paper Brand by Code."""

        return (
            self.db.query(PaperBrand)
            .filter(
                PaperBrand.brand_code == brand_code
            )
            .first()
        )

    def get_by_name(
        self,
        brand_name: str,
    ) -> PaperBrand | None:
        """Get Paper Brand by Name."""

        return (
            self.db.query(PaperBrand)
            .filter(
                PaperBrand.brand_name == brand_name
            )
            .first()
        )

    def update(
        self,
        db_paper_brand: PaperBrand,
        paper_brand: PaperBrandUpdate,
    ) -> PaperBrand:
        """Update Paper Brand."""

        update_data = paper_brand.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_paper_brand,
                key,
                value,
            )

        self.db.commit()
        self.db.refresh(db_paper_brand)

        return db_paper_brand

    def delete(
        self,
        db_paper_brand: PaperBrand,
    ) -> None:
        """Delete Paper Brand."""

        self.db.delete(db_paper_brand)
        self.db.commit()

    def search(
        self,
        keyword: str,
    ) -> list[PaperBrand]:
        """Search Paper Brands."""

        return (
            self.db.query(PaperBrand)
            .filter(
                or_(
                    PaperBrand.brand_code.ilike(
                        f"%{keyword}%"
                    ),
                    PaperBrand.brand_name.ilike(
                        f"%{keyword}%"
                    ),
                    PaperBrand.manufacturer.ilike(
                        f"%{keyword}%"
                    ),
                    PaperBrand.country.ilike(
                        f"%{keyword}%"
                    ),
                )
            )
            .order_by(
                PaperBrand.display_order,
                PaperBrand.brand_name,
            )
            .all()
        )