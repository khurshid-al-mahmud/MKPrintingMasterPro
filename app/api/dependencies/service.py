from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db

from app.repositories.party_repository import PartyRepository
from app.repositories.supplier_repository import SupplierRepository

from app.services.party_service import PartyService
from app.services.supplier_service import SupplierService


def get_party_service(
    db: Session = Depends(get_db),
) -> PartyService:
    repository = PartyRepository(db)

    return PartyService(
        repository=repository,
    )


def get_supplier_service(
    db: Session = Depends(get_db),
) -> SupplierService:
    repository = SupplierRepository(db)

    return SupplierService(
        repository=repository,
    )