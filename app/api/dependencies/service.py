"""
Service Dependencies.

Shared service dependencies
for the entire ERP system.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db


# ==========================
# Repositories
# ==========================

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
from app.repositories.product_template_repository import ProductTemplateRepository
from app.repositories.product_category_repository import ProductCategoryRepository
from app.repositories.supplier_repository import SupplierRepository

from app.repositories.specification_group_repository import (
    SpecificationGroupRepository,
)

from app.repositories.specification_field_repository import (
    SpecificationFieldRepository,
)

from app.repositories.field_option_repository import (
    FieldOptionRepository,
)

from app.repositories.validation_rule_repository import (
    ValidationRuleRepository,
)

# ==========================
# Services
# ==========================

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
from app.services.product_template_service import ProductTemplateService
from app.services.product_category_service import ProductCategoryService
from app.services.supplier_service import SupplierService

from app.services.specification_group_service import (
    SpecificationGroupService,
)

from app.services.specification_field_service import (
    SpecificationFieldService,
)

from app.services.field_option_service import (
    FieldOptionService,
)

from app.services.validation_rule_service import (
    ValidationRuleService,
)

# ==========================
# Party
# ==========================

def get_party_service(
    db: Session = Depends(get_db),
) -> PartyService:

    return PartyService(
        PartyRepository(db),
    )



# ==========================
# Supplier
# ==========================

def get_supplier_service(
    db: Session = Depends(get_db),
) -> SupplierService:

    return SupplierService(
        SupplierRepository(db),
    )



# ==========================
# Customer
# ==========================

def get_customer_service(
    db: Session = Depends(get_db),
) -> CustomerService:

    return CustomerService(
        CustomerRepository(db),
    )



# ==========================
# Employee
# ==========================

def get_employee_service(
    db: Session = Depends(get_db),
) -> EmployeeService:

    return EmployeeService(
        EmployeeRepository(db),
    )



# ==========================
# Print Partner
# ==========================

def get_print_partner_service(
    db: Session = Depends(get_db),
) -> PrintPartnerService:

    return PrintPartnerService(
        PrintPartnerRepository(db),
    )



# ==========================
# Machine
# ==========================

def get_machine_service(
    db: Session = Depends(get_db),
) -> MachineService:

    return MachineService(
        MachineRepository(db),
    )



# ==========================
# Product
# ==========================

def get_product_service(
    db: Session = Depends(get_db),
) -> ProductService:

    return ProductService(
        ProductRepository(db),
    )



# ==========================
# Product Template
# ==========================

def get_product_template_service(
    db: Session = Depends(get_db),
) -> ProductTemplateService:

    return ProductTemplateService(
        ProductTemplateRepository(db),
    )



# ==========================
# Product Category
# ==========================

def get_product_category_service(
    db: Session = Depends(get_db),
) -> ProductCategoryService:

    return ProductCategoryService(
        ProductCategoryRepository(db),
    )



# ==========================
# Paper Type
# ==========================

def get_paper_type_service(
    db: Session = Depends(get_db),
) -> PaperTypeService:

    return PaperTypeService(
        PaperTypeRepository(db),
    )



# ==========================
# Paper Brand
# ==========================

def get_paper_brand_service(
    db: Session = Depends(get_db),
) -> PaperBrandService:

    return PaperBrandService(
        PaperBrandRepository(db),
    )



# ==========================
# Paper GSM
# ==========================

def get_paper_gsm_service(
    db: Session = Depends(get_db),
) -> PaperGSMService:

    return PaperGSMService(
        PaperGSMRepository(db),
    )



# ==========================
# Paper Size
# ==========================

def get_paper_size_service(
    db: Session = Depends(get_db),
) -> PaperSizeService:

    return PaperSizeService(
        PaperSizeRepository(db),
    )



# ==================================================
# Specification Group
# ==================================================

def get_specification_group_service(
    db: Session = Depends(get_db),
) -> SpecificationGroupService:

    return SpecificationGroupService(
        SpecificationGroupRepository(db),
    )



# ==================================================
# Specification Field
# ==================================================

def get_specification_field_service(
    db: Session = Depends(get_db),
) -> SpecificationFieldService:

    return SpecificationFieldService(
        SpecificationFieldRepository(db),
    )
# ==================================================
# Field Option
# ==================================================

def get_field_option_service(
    db: Session = Depends(get_db),
) -> FieldOptionService:

    return FieldOptionService(
        FieldOptionRepository(db),
    )

# ==================================================
# Validation Rule
# ==================================================

def get_validation_rule_service(
    db: Session = Depends(get_db),
) -> ValidationRuleService:

    return ValidationRuleService(
        ValidationRuleRepository(db),
    )