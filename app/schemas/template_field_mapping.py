"""
MKPrintingMasterPro ERP
Build-016

Template Field Mapping Schema

Purpose:
Pydantic schemas for Template Field Mapping API.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ======================================
# Base
# ======================================

class TemplateFieldMappingBase(BaseModel):

    template_id: int

    field_id: int

    is_required: bool = False

    is_visible: bool = True

    is_editable: bool = True

    default_value: str | None = None

    display_order: int = 1

    group_order: int = 1

    column_width: int = 12

    show_in_quotation: bool = True

    show_in_job_order: bool = True

    show_in_production: bool = True

    show_in_invoice: bool = False

    validation_override: str | None = None

    formula_override: str | None = None

    is_active: bool = True



# ======================================
# Create
# ======================================

class TemplateFieldMappingCreate(
    TemplateFieldMappingBase
):
    pass



# ======================================
# Update
# ======================================

class TemplateFieldMappingUpdate(
    BaseModel
):

    is_required: bool | None = None

    is_visible: bool | None = None

    is_editable: bool | None = None

    default_value: str | None = None

    display_order: int | None = None

    group_order: int | None = None

    column_width: int | None = None

    show_in_quotation: bool | None = None

    show_in_job_order: bool | None = None

    show_in_production: bool | None = None

    show_in_invoice: bool | None = None

    validation_override: str | None = None

    formula_override: str | None = None

    is_active: bool | None = None



# ======================================
# Response
# ======================================

class TemplateFieldMappingResponse(
    TemplateFieldMappingBase
):

    id: int

    created_by: str | None = None

    updated_by: str | None = None

    created_at: datetime | None = None

    updated_at: datetime | None = None


    model_config = ConfigDict(
        from_attributes=True
    )