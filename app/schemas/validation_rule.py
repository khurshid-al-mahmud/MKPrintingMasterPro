"""
MKPrintingMasterPro ERP

Build-013

Validation Rule Schemas

Purpose:
Pydantic schemas for Validation Rule Management.

Status:
Production Ready
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ==================================================
# Base Schema
# ==================================================

class ValidationRuleBase(BaseModel):
    """
    Common Validation Rule fields.
    """

    field_id: int

    rule_code: str

    rule_name: str

    description: str | None = None

    validation_type: str

    minimum_value: str | None = None

    maximum_value: str | None = None

    regex_pattern: str | None = None

    validation_expression: str | None = None

    error_message: str | None = None

    stop_processing: bool = True

    is_active: bool = True


# ==================================================
# Create Schema
# ==================================================

class ValidationRuleCreate(
    ValidationRuleBase
):
    """
    Create Validation Rule.
    """

    pass


# ==================================================
# Update Schema
# ==================================================

class ValidationRuleUpdate(BaseModel):
    """
    Update Validation Rule.
    """

    rule_name: str | None = None

    description: str | None = None

    validation_type: str | None = None

    minimum_value: str | None = None

    maximum_value: str | None = None

    regex_pattern: str | None = None

    validation_expression: str | None = None

    error_message: str | None = None

    stop_processing: bool | None = None

    is_active: bool | None = None


# ==================================================
# Response Schema
# ==================================================

class ValidationRuleResponse(
    ValidationRuleBase
):
    """
    Response Schema.
    """

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    created_by: str | None = None

    updated_by: str | None = None

    created_at: datetime

    updated_at: datetime