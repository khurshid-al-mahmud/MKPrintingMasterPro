"""
Service Dependencies.

Shared service dependencies
for the entire ERP system.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.repositories.party_repository import PartyRepository
from app.services.party_service import PartyService


def get_party_service(
    db: Session = Depends(get_db),
) -> PartyService:
    """
    Provide PartyService dependency.
    """

    repository = PartyRepository(db)

    return PartyService(repository)