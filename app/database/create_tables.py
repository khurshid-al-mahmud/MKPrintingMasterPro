from app.database.engine import engine
from app.models.base import Base


# =====================================
# Import ALL models
# This registers every mapper
# =====================================

from app.models import (

    # Core
    NumberSequence,

    Party,
    PartyContact,
    PartyRole,

    CustomerProfile,
    SupplierProfile,
    EmployeeProfile,
    PrintPartnerProfile,


    # Production Masters
    PaperSize,
    PaperBrand,
    BindingType,

    CompanyProfile,
    SystemSetting,
    Machine,


    # Product Management
    Product,
    ProductCategory,
    ProductTemplate,


    # Dynamic Specification Engine
    SpecificationGroup,
    FieldOption,
    SpecificationField,
    TemplateFieldMapping,
    SpecificationDependencyRule,
    FormulaRule,
    TemplateVersion,
    SpecificationAudit,
    ValidationRule,
)



def create_tables():

    print("Creating database tables...")


    Base.metadata.create_all(
        bind=engine
    )


    print("Database tables created successfully!")



if __name__ == "__main__":

    create_tables()