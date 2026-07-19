"""
Paper GSM Repository.

Database operations for
Paper GSM Master.
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.paper_gsm import PaperGSM
from app.schemas.paper_gsm import PaperGSMCreate
from app.schemas.paper_gsm import PaperGSMUpdate


class PaperGSMRepository:
    """Paper GSM Repository."""

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        paper_gsm: PaperGSMCreate,
    ) -> PaperGSM:
        """Create Paper GSM."""

        db_paper_gsm = PaperGSM(
            **paper_gsm.model_dump()
        )

        self.db.add(db_paper_gsm)
        self.db.commit()
        self.db.refresh(db_paper_gsm)

        return db_paper_gsm

    def get_all(self) -> list[PaperGSM]:
        """Get all Paper GSM."""

        return (
            self.db.query(PaperGSM)
            .order_by(
                PaperGSM.display_order,
                PaperGSM.gsm_value,
            )
            .all()
        )

    def get_active(self) -> list[PaperGSM]:
        """Get active Paper GSM."""

        return (
            self.db.query(PaperGSM)
            .filter(
                PaperGSM.is_active.is_(True)
            )
            .order_by(
                PaperGSM.display_order,
                PaperGSM.gsm_value,
            )
            .all()
        )

    def get_by_id(
        self,
        paper_gsm_id: int,
    ) -> PaperGSM | None:
        """Get Paper GSM by ID."""

        return (
            self.db.query(PaperGSM)
            .filter(
                PaperGSM.id == paper_gsm_id
            )
            .first()
        )

    def get_by_code(
        self,
        gsm_code: str,
    ) -> PaperGSM | None:
        """Get Paper GSM by Code."""

        return (
            self.db.query(PaperGSM)
            .filter(
                PaperGSM.gsm_code == gsm_code
            )
            .first()
        )

    def get_by_name(
        self,
        gsm_name: str,
    ) -> PaperGSM | None:
        """Get Paper GSM by Name."""

        return (
            self.db.query(PaperGSM)
            .filter(
                PaperGSM.gsm_name == gsm_name
            )
            .first()
        )

    def update(
        self,
        db_paper_gsm: PaperGSM,
        paper_gsm: PaperGSMUpdate,
    ) -> PaperGSM:
        """Update Paper GSM."""

        update_data = paper_gsm.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_paper_gsm,
                key,
                value,
            )

        self.db.commit()
        self.db.refresh(db_paper_gsm)

        return db_paper_gsm

    def delete(
        self,
        db_paper_gsm: PaperGSM,
    ) -> None:
        """Delete Paper GSM."""

        self.db.delete(db_paper_gsm)
        self.db.commit()

    def search(
        self,
        keyword: str,
    ) -> list[PaperGSM]:
        """Search Paper GSM."""

        return (
            self.db.query(PaperGSM)
            .filter(
                or_(
                    PaperGSM.gsm_code.ilike(
                        f"%{keyword}%"
                    ),
                    PaperGSM.gsm_name.ilike(
                        f"%{keyword}%"
                    ),
                    PaperGSM.paper_category.ilike(
                        f"%{keyword}%"
                    ),
                )
            )
            .order_by(
                PaperGSM.display_order,
                PaperGSM.gsm_value,
            )
            .all()
        )