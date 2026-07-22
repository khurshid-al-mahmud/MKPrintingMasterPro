"""
Company Profile Service.

Business Logic Layer
for Company Profile.
"""

from app.repositories.company_profile_repository import (
    CompanyProfileRepository,
)
from app.schemas.company_profile import (
    CompanyProfileCreate,
    CompanyProfileUpdate,
)


class CompanyProfileService:
    """Company Profile Service."""

    def __init__(
        self,
        repository: CompanyProfileRepository,
    ):
        self.repository = repository

    def create(
        self,
        company: CompanyProfileCreate,
    ):
        """
        Create Company Profile.
        """

        existing = self.repository.get()

        if existing:
            raise ValueError(
                "Company Profile already exists."
            )

        return self.repository.create(
            company
        )

    def get(self):
        """
        Get Company Profile.
        """

        return self.repository.get()

    def get_by_id(
        self,
        company_id: int,
    ):
        """
        Get Company Profile by ID.
        """

        db_company = self.repository.get_by_id(
            company_id
        )

        if not db_company:
            raise ValueError(
                "Company Profile not found."
            )

        return db_company

    def update(
        self,
        company_id: int,
        company: CompanyProfileUpdate,
    ):
        """
        Update Company Profile.
        """

        db_company = self.repository.get_by_id(
            company_id
        )

        if not db_company:
            raise ValueError(
                "Company Profile not found."
            )

        return self.repository.update(
            db_company,
            company,
        )

    def delete(
        self,
        company_id: int,
    ):
        """
        Delete Company Profile.
        """

        db_company = self.repository.get_by_id(
            company_id
        )

        if not db_company:
            raise ValueError(
                "Company Profile not found."
            )

        self.repository.delete(
            db_company
        )

        return {
            "message": "Company Profile deleted successfully."
        }