"""
MKPrintingMasterPro ERP

Central Model Registry
"""


# ===========================
# Core Models
# ===========================

from .number_sequence import NumberSequence

from .party import Party
from .party_contact import PartyContact
from .party_role import PartyRole

from .customer_profile import CustomerProfile
from .supplier_profile import SupplierProfile
from .employee_profile import EmployeeProfile
from .print_partner_profile import PrintPartnerProfile



# ===========================
# Paper & Production Masters
# ===========================

from .paper_size import PaperSize
from .paper_brand import PaperBrand
from .binding_type import BindingType

from .company_profile import CompanyProfile
from .system_setting import SystemSetting
from .machine import Machine



# ===========================
# Product Management
# ===========================

from .product import Product
from .product_category import ProductCategory

from .product_template import ProductTemplate

from .quotation_master import QuotationMaster
from .quotation_item import QuotationItem

from .invoice_master import InvoiceMaster
from .invoice_item import InvoiceItem



# ===========================
# Build-030 Job Order
# ===========================

from .job_order_master import JobOrderMaster
from .job_order_item import JobOrderItem
from .job_order_status_history import JobOrderStatusHistory



# ===========================
# Dynamic Specification Engine
# ===========================

from .specification_group import SpecificationGroup

from .field_option import FieldOption

from .specification_field import SpecificationField

from .template_field_mapping import TemplateFieldMapping

from .specification_dependency_rule import SpecificationDependencyRule

from .formula_rule import FormulaRule

from .template_version import TemplateVersion

from .specification_audit import SpecificationAudit

from .validation_rule import ValidationRule



__all__ = [

    # ===========================
    # Core
    # ===========================

    "NumberSequence",

    "Party",
    "PartyContact",
    "PartyRole",

    "CustomerProfile",
    "SupplierProfile",
    "EmployeeProfile",
    "PrintPartnerProfile",



    # ===========================
    # Masters
    # ===========================

    "PaperSize",
    "PaperBrand",
    "BindingType",

    "CompanyProfile",
    "SystemSetting",
    "Machine",



    # ===========================
    # Product Management
    # ===========================

    "Product",
    "ProductCategory",
    "ProductTemplate",

    "QuotationMaster",
    "QuotationItem",

    "InvoiceMaster",
    "InvoiceItem",



    # ===========================
    # Build-030 Job Order
    # ===========================

    "JobOrderMaster",
    "JobOrderItem",
    "JobOrderStatusHistory",



    # ===========================
    # Dynamic Specification Engine
    # ===========================

    "SpecificationGroup",

    "FieldOption",

    "SpecificationField",

    "TemplateFieldMapping",

    "SpecificationDependencyRule",

    "FormulaRule",

    "TemplateVersion",

    "SpecificationAudit",

    "ValidationRule",
]