"""
Formula Rule Schemas.

Used for creating, updating and returning
Formula Rule data.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


# ==========================================
# Base
# ==========================================

class FormulaRuleBase(BaseModel):
    """
    Common fields.
    """

    template_id: int

    formula_code: str

    formula_name_en: str

    formula_name_bn: str | None = None

    description: str | None = None

    formula_type: str

    formula_expression: str

    version: str | None = None

    effective_date: datetime | None = None

    is_default: bool = False

    is_active: bool = True


# ==========================================
# Create
# ==========================================

class FormulaRuleCreate(
    FormulaRuleBase
):
    """
    Create Schema.
    """

    pass


# ==========================================
# Update
# ==========================================

class FormulaRuleUpdate(BaseModel):
    """
    Update Schema.
    """

    template_id: int | None = None

    formula_code: str | None = None

    formula_name_en: str | None = None

    formula_name_bn: str | None = None

    description: str | None = None

    formula_type: str | None = None

    formula_expression: str | None = None

    version: str | None = None

    effective_date: datetime | None = None

    is_default: bool | None = None

    is_active: bool | None = None


# ==========================================
# Response
# ==========================================

class FormulaRuleResponse(
    FormulaRuleBase
):
    """
    Response Schema.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    created_by: str | None = None

    updated_by: str | None = None

    created_at: datetime | None = None

    updated_at: datetime | None = None