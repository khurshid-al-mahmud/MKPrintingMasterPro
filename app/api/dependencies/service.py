"""
Service Dependency Provider.

Central place for
injecting service classes.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db


# =========================
# Party Service
# =========================

from app.services.party_service import PartyService
from app.repositories.party_repository import PartyRepository


def get_party_service(
    db: Session = Depends(get_db),
):
    repository = PartyRepository(db)

    return PartyService(
        repository
    )


# =========================
# Supplier Service
# =========================

from app.services.supplier_service import SupplierService
from app.repositories.supplier_repository import SupplierRepository


def get_supplier_service(
    db: Session = Depends(get_db),
):
    repository = SupplierRepository(db)

    return SupplierService(
        repository
    )


# =========================
# Customer Service
# =========================

from app.services.customer_service import CustomerService
from app.repositories.customer_repository import CustomerRepository


def get_customer_service(
    db: Session = Depends(get_db),
):
    repository = CustomerRepository(db)

    return CustomerService(
        repository
    )


# =========================
# Employee Service
# =========================

from app.services.employee_service import EmployeeService
from app.repositories.employee_repository import EmployeeRepository


def get_employee_service(
    db: Session = Depends(get_db),
):
    repository = EmployeeRepository(db)

    return EmployeeService(
        repository
    )


# =========================
# Print Partner Service
# =========================

from app.services.print_partner_service import PrintPartnerService
from app.repositories.print_partner_repository import PrintPartnerRepository


def get_print_partner_service(
    db: Session = Depends(get_db),
):
    repository = PrintPartnerRepository(db)

    return PrintPartnerService(
        repository
    )