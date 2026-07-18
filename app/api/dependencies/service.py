"""
Service Dependencies.

Shared service dependencies
for the entire ERP system.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db

from app.repositories.customer_repository import CustomerRepository
from app.repositories.employee_repository import EmployeeRepository
from app.repositories.party_repository import PartyRepository
from app.repositories.supplier_repository import SupplierRepository

from app.services.customer_service import CustomerService
from app.services.employee_service import EmployeeService
from app.services.party_service import PartyService
from app.services.supplier_service import SupplierService


def get_party_service(
    db: Session = Depends(get_db),
) -> PartyService:
    """
    Provide PartyService dependency.
    """

    return PartyService(
        PartyRepository(db),
    )


def get_supplier_service(
    db: Session = Depends(get_db),
) -> SupplierService:
    """
    Provide SupplierService dependency.
    """

    return SupplierService(
        SupplierRepository(db),
    )


def get_customer_service(
    db: Session = Depends(get_db),
) -> CustomerService:
    """
    Provide CustomerService dependency.
    """

    return CustomerService(
        CustomerRepository(db),
    )


def get_employee_service(
    db: Session = Depends(get_db),
) -> EmployeeService:
    """
    Provide EmployeeService dependency.
    """

    return EmployeeService(
        EmployeeRepository(db),
    )