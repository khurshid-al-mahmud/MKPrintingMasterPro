"""
MKPrintingMasterPro ERP

Central Model Registry
"""

# Existing Core Models
from .number_sequence import NumberSequence
from .party import Party
from .party_contact import PartyContact
from .party_role import PartyRole

from .customer_profile import CustomerProfile
from .supplier_profile import SupplierProfile
from .employee_profile import EmployeeProfile
from .print_partner_profile import PrintPartnerProfile

from .paper_size import PaperSize
from .paper_brand import PaperBrand

from .binding_type import BindingType
from .company_profile import CompanyProfile
from .system_setting import SystemSetting
from .machine import Machine

# Dynamic Specification Engine
from .product_template import ProductTemplate
from .specification_group import SpecificationGroup
from .specification_field import SpecificationField
from .field_option import FieldOption
from .template_field_mapping import TemplateFieldMapping
from .specification_dependency_rule import SpecificationDependencyRule
from .formula_rule import FormulaRule
from .template_version import TemplateVersion
from .specification_audit import SpecificationAudit
from .validation_rule import ValidationRule

__all__ = [
    "NumberSequence",
    "Party",
    "PartyContact",
    "PartyRole",
    "CustomerProfile",
    "SupplierProfile",
    "EmployeeProfile",
    "PrintPartnerProfile",
    "PaperSize",
    "PaperBrand",
    "BindingType",
    "CompanyProfile",
    "SystemSetting",
    "Machine",

    "ProductTemplate",
    "SpecificationGroup",
    "SpecificationField",
    "FieldOption",
    "TemplateFieldMapping",
    "SpecificationDependencyRule",
    "FormulaRule",
    "TemplateVersion",
    "SpecificationAudit",
    "ValidationRule",
]