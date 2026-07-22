"""
Company Profile Repository.
"""

from sqlalchemy.orm import Session

from app.models.company_profile import CompanyProfile
from app.schemas.company_profile import CompanyProfileCreate
from app.schemas.company_profile import CompanyProfileUpdate


class CompanyProfileRepository:
    """Company Profile Repository."""

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        company: CompanyProfileCreate,
    ) -> CompanyProfile:

        db_company = CompanyProfile(
            **company.model_dump()
        )

        self.db.add(db_company)
        self.db.commit()
        self.db.refresh(db_company)

        return db_company

    def get(self) -> CompanyProfile | None:

        return (
            self.db.query(CompanyProfile)
            .first()
        )

    def get_by_id(
        self,
        company_id: int,
    ) -> CompanyProfile | None:

        return (
            self.db.query(CompanyProfile)
            .filter(
                CompanyProfile.id == company_id
            )
            .first()
        )

    def update(
        self,
        db_company: CompanyProfile,
        company: CompanyProfileUpdate,
    ) -> CompanyProfile:

        update_data = company.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_company,
                key,
                value,
            )

        self.db.commit()
        self.db.refresh(db_company)

        return db_company

    def delete(
        self,
        db_company: CompanyProfile,
    ) -> None:

        self.db.delete(db_company)
        self.db.commit()