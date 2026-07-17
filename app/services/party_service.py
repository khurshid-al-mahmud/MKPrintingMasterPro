"""
Party Service.

Business Logic Layer
for Party Management.
"""

from app.models.party import Party
from app.repositories.party_repository import PartyRepository
from app.schemas.party import PartyCreate, PartyUpdate


class PartyService:
    """
    Service layer for Party management.
    """

    def __init__(
        self,
        repository: PartyRepository,
    ) -> None:
        self.repository = repository

    def create(
        self,
        party: PartyCreate,
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

        new_party = Party(
            party_name=party.party_name,
            mobile=party.mobile,
            email=party.email,
            address=party.address,
        )

        return self.repository.create(
            new_party,
        )

    def get_by_id(
        self,
        party_id: int,
    ) -> Party | None:
        """
        Get party by ID.
        """

        return self.repository.get_by_id(
            party_id,
        )

    def get_all(
        self,
    ) -> list[Party]:
        """
        Get all active parties.
        """

        return self.repository.get_all()

    def update(
        self,
        party_id: int,
        party_data: PartyUpdate,
    ) -> Party | None:
        """
        Update existing party.
        """

        return self.repository.update(
            party_id,
            party_data.model_dump(
                exclude_unset=True,
            ),
        )

    def delete(
        self,
        party_id: int,
    ) -> bool:
        """
        Soft delete party.
        """

        return self.repository.soft_delete(
            party_id,
        )

    def search(
        self,
        keyword: str,
    ) -> list[Party]:
        """
        Search parties.
        """

        return self.repository.search(
            keyword,
        )