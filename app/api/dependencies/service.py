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
from app.repositories.machine_repository import MachineRepository
from app.repositories.paper_brand_repository import PaperBrandRepository
from app.repositories.paper_gsm_repository import PaperGSMRepository
from app.repositories.paper_size_repository import PaperSizeRepository
from app.repositories.paper_type_repository import PaperTypeRepository
from app.repositories.party_repository import PartyRepository
from app.repositories.print_partner_repository import PrintPartnerRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.supplier_repository import SupplierRepository

from app.services.customer_service import CustomerService
from app.services.employee_service import EmployeeService
from app.services.machine_service import MachineService
from app.services.paper_brand_service import PaperBrandService
from app.services.paper_gsm_service import PaperGSMService
from app.services.paper_size_service import PaperSizeService
from app.services.paper_type_service import PaperTypeService
from app.services.party_service import PartyService
from app.services.print_partner_service import PrintPartnerService
from app.services.product_service import ProductService
from app.services.supplier_service import SupplierService


def get_party_service(
    db: Session = Depends(get_db),
) -> PartyService:
    """Provide PartyService dependency."""

    return PartyService(
        PartyRepository(db),
    )


def get_supplier_service(
    db: Session = Depends(get_db),
) -> SupplierService:
    """Provide SupplierService dependency."""

    return SupplierService(
        SupplierRepository(db),
    )


def get_customer_service(
    db: Session = Depends(get_db),
) -> CustomerService:
    """Provide CustomerService dependency."""

    return CustomerService(
        CustomerRepository(db),
    )


def get_employee_service(
    db: Session = Depends(get_db),
) -> EmployeeService:
    """Provide EmployeeService dependency."""

    return EmployeeService(
        EmployeeRepository(db),
    )


def get_print_partner_service(
    db: Session = Depends(get_db),
) -> PrintPartnerService:
    """Provide PrintPartnerService dependency."""

    return PrintPartnerService(
        PrintPartnerRepository(db),
    )


def get_machine_service(
    db: Session = Depends(get_db),
) -> MachineService:
    """Provide MachineService dependency."""

    return MachineService(
        MachineRepository(db),
    )


def get_product_service(
    db: Session = Depends(get_db),
) -> ProductService:
    """Provide ProductService dependency."""

    return ProductService(
        ProductRepository(db),
    )


def get_paper_type_service(
    db: Session = Depends(get_db),
) -> PaperTypeService:
    """Provide PaperTypeService dependency."""

    return PaperTypeService(
        PaperTypeRepository(db),
    )


def get_paper_brand_service(
    db: Session = Depends(get_db),
) -> PaperBrandService:
    """Provide PaperBrandService dependency."""

    return PaperBrandService(
        PaperBrandRepository(db),
    )


def get_paper_gsm_service(
    db: Session = Depends(get_db),
) -> PaperGSMService:
    """Provide PaperGSMService dependency."""

    return PaperGSMService(
        PaperGSMRepository(db),
    )


def get_paper_size_service(
    db: Session = Depends(get_db),
) -> PaperSizeService:
    """Provide PaperSizeService dependency."""

    return PaperSizeService(
        PaperSizeRepository(db),
    )