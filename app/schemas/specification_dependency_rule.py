"""
MKPrintingMasterPro ERP
Build-013

Specification Dependency Rule Schema

Purpose:
Pydantic schemas for Dependency Rule API.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ======================================
# Base
# ======================================

class SpecificationDependencyRuleBase(BaseModel):

    template_id: int

    source_field_id: int

    trigger_value: str

    target_field_id: int

    action: str

    description: str | None = None

    priority: int = 1

    is_active: bool = True


# ======================================
# Create
# ======================================

class SpecificationDependencyRuleCreate(
    SpecificationDependencyRuleBase
):
    pass


# ======================================
# Update
# ======================================

class SpecificationDependencyRuleUpdate(
    BaseModel
):

    trigger_value: str | None = None

    action: str | None = None

    description: str | None = None

    priority: int | None = None

    is_active: bool | None = None


# ======================================
# Response
# ======================================

class SpecificationDependencyRuleResponse(
    SpecificationDependencyRuleBase
):

    id: int

    created_by: str | None = None

    updated_by: str | None = None

    created_at: datetime | None = None

    updated_at: datetime | None = None


    model_config = ConfigDict(
        from_attributes=True
    )