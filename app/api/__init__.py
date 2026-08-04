"""
API Routers.

Exports all API routers.
"""

from .binding_type import router as binding_type_router
from .company_profile import router as company_profile_router
from .customer import router as customer_router
from .employee import router as employee_router
from .machine import router as machine_router
from .paper_brand import router as paper_brand_router
from .paper_gsm import router as paper_gsm_router
from .paper_size import router as paper_size_router
from .paper_type import router as paper_type_router
from .party import router as party_router
from .print_partner import router as print_partner_router
from .product import router as product_router
from .product_category import router as product_category_router
from .product_template import router as product_template_router
from .supplier import router as supplier_router
from .system_setting import router as system_setting_router

from .specification_group import router as specification_group_router
from .specification_field import router as specification_field_router
from .field_option import router as field_option_router
from .validation_rule import router as validation_rule_router
from .formula_rule import router as formula_rule_router


__all__ = [
    "binding_type_router",
    "company_profile_router",
    "customer_router",
    "employee_router",
    "machine_router",
    "paper_brand_router",
    "paper_gsm_router",
    "paper_size_router",
    "paper_type_router",
    "party_router",
    "print_partner_router",
    "product_router",
    "product_category_router",
    "product_template_router",
    "supplier_router",
    "system_setting_router",

    "specification_group_router",
    "specification_field_router",
    "field_option_router",
    "validation_rule_router",
    "formula_rule_router",
]