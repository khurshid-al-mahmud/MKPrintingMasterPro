"""
Party Service.

Business Logic Layer
for Party Management.
"""

from app.models.party import Party
from app.repositories.party_repository import (
    PartyRepository,
)


class PartyService:
    """Business logic for Party."""

    def __init__(
        self,
        repository: PartyRepository,
    ) -> None:
        self.repository = repository

    def create_party(
        self,
        party: Party,
    ) -> Party:
        """
        Create new party.
        """

        if self.repository.exists_by_name(
            party.party_name,
        ):
            raise ValueError(
                "Party name already exists."
            )

        if (
            party.mobile
            and self.repository.exists_by_mobile(
                party.mobile,
            )
        ):
            raise ValueError(
                "Mobile number already exists."
            )

        return self.repository.create(
            party,
        )








    def get_party(
        self,
        party_id: int,
    ) -> Party | None:
        """
        Get party by ID.
        """

        return self.repository.get_by_id(
            party_id,
        )

    def get_all_parties(
        self,
    ) -> list[Party]:
        """
        Get all active parties.
        """

        return self.repository.get_all()

    def update_party(
        self,
        party_id: int,
        party_data: dict,
    ) -> Party | None:
        """
        Update existing party.
        """

        return self.repository.update(
            party_id,
            party_data,
        )








    def delete_party(
        self,
        party_id: int,
    ) -> bool:
        """
        Soft delete party.
        """

        return self.repository.soft_delete(
            party_id,
        )

    def search_parties(
        self,
        keyword: str,
    ) -> list[Party]:
        """
        Search parties.
        """

        return self.repository.search(
            keyword,
        )