"""
Import all SQLAlchemy models.

This ensures all models are registered with Base.metadata.
"""

from app.models.binding_type import BindingType
from app.models.company_profile import CompanyProfile
from app.models.customer_profile import CustomerProfile
from app.models.employee_profile import EmployeeProfile
from app.models.machine import Machine
from app.models.number_sequence import NumberSequence
from app.models.paper_brand import PaperBrand
from app.models.paper_gsm import PaperGSM
from app.models.paper_size import PaperSize
from app.models.paper_type import PaperType
from app.models.party import Party
from app.models.party_contact import PartyContact
from app.models.party_role import PartyRole
from app.models.print_partner_profile import PrintPartnerProfile
from app.models.product import Product
from app.models.supplier_profile import SupplierProfile
from app.models.system_setting import SystemSetting

__all__ = [
    "BindingType",
    "CompanyProfile",
    "CustomerProfile",
    "EmployeeProfile",
    "Machine",
    "NumberSequence",
    "PaperBrand",
    "PaperGSM",
    "PaperSize",
    "PaperType",
    "Party",
    "PartyContact",
    "PartyRole",
    "PrintPartnerProfile",
    "Product",
    "SupplierProfile",
    "SystemSetting",
]