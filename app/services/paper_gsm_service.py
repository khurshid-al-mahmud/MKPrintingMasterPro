"""
Paper GSM Service.

Contains all business logic
for Paper GSM Master.
"""

from app.repositories.paper_gsm_repository import PaperGSMRepository
from app.schemas.paper_gsm import PaperGSMCreate
from app.schemas.paper_gsm import PaperGSMUpdate


class PaperGSMService:
    """Paper GSM Service."""

    def __init__(self, repository: PaperGSMRepository):
        self.repository = repository

    def create(self, paper_gsm: PaperGSMCreate):
        """Create Paper GSM."""

        existing_code = self.repository.get_by_code(
            paper_gsm.gsm_code
        )

        if existing_code:
            raise ValueError(
                "Paper GSM Code already exists."
            )

        existing_name = self.repository.get_by_name(
            paper_gsm.gsm_name
        )

        if existing_name:
            raise ValueError(
                "Paper GSM Name already exists."
            )

        return self.repository.create(paper_gsm)

    def get_all(self):
        """Get all Paper GSM."""

        return self.repository.get_all()

    def get_active(self):
        """Get active Paper GSM."""

        return self.repository.get_active()

    def get_by_id(self, paper_gsm_id: int):
        """Get Paper GSM by ID."""

        paper_gsm = self.repository.get_by_id(
            paper_gsm_id
        )

        if not paper_gsm:
            raise ValueError(
                "Paper GSM not found."
            )

        return paper_gsm

    def update(
        self,
        paper_gsm_id: int,
        paper_gsm: PaperGSMUpdate,
    ):
        """Update Paper GSM."""

        db_paper_gsm = self.repository.get_by_id(
            paper_gsm_id
        )

        if not db_paper_gsm:
            raise ValueError(
                "Paper GSM not found."
            )

        if (
            paper_gsm.gsm_code
            and paper_gsm.gsm_code
            != db_paper_gsm.gsm_code
        ):
            existing_code = self.repository.get_by_code(
                paper_gsm.gsm_code
            )

            if existing_code:
                raise ValueError(
                    "Paper GSM Code already exists."
                )

        if (
            paper_gsm.gsm_name
            and paper_gsm.gsm_name
            != db_paper_gsm.gsm_name
        ):
            existing_name = self.repository.get_by_name(
                paper_gsm.gsm_name
            )

            if existing_name:
                raise ValueError(
                    "Paper GSM Name already exists."
                )

        return self.repository.update(
            db_paper_gsm,
            paper_gsm,
        )

    def delete(self, paper_gsm_id: int):
        """Delete Paper GSM."""

        db_paper_gsm = self.repository.get_by_id(
            paper_gsm_id
        )

        if not db_paper_gsm:
            raise ValueError(
                "Paper GSM not found."
            )

        self.repository.delete(db_paper_gsm)

    def search(self, keyword: str):
        """Search Paper GSM."""

        return self.repository.search(keyword)