"""
Field Option Schemas.

Used for creating, updating and returning
Dynamic Field Option data.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class FieldOptionBase(BaseModel):
    """
    Common fields for Field Option.
    """

    field_id: int

    option_code: str

    option_name_en: str

    option_name_bn: str | None = None

    description: str | None = None

    option_value: str

    display_order: int = 1

    is_default: bool = False

    is_active: bool = True


class FieldOptionCreate(FieldOptionBase):
    """
    Create Field Option.
    """

    pass


class FieldOptionUpdate(BaseModel):
    """
    Update Field Option.
    """

    option_code: str | None = None

    option_name_en: str | None = None

    option_name_bn: str | None = None

    description: str | None = None

    option_value: str | None = None

    display_order: int | None = None

    is_default: bool | None = None

    is_active: bool | None = None


class FieldOptionResponse(FieldOptionBase):
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