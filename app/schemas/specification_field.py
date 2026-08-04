"""
Specification Field Schemas.

Used for creating, updating and returning
Dynamic Specification Field data.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SpecificationFieldBase(BaseModel):
    """
    Common fields for Specification Field.
    """

    field_code: str

    field_name_en: str

    field_name_bn: str | None = None

    description: str | None = None

    group_id: int

    data_type: str

    input_control: str

    placeholder_en: str | None = None

    placeholder_bn: str | None = None

    default_value: str | None = None

    help_text: str | None = None

    icon: str | None = None

    is_required: bool = False

    is_editable: bool = True

    is_visible: bool = True

    is_calculated: bool = False

    is_system_field: bool = False

    display_order: int = 1

    width: int = 12

    minimum_value: str | None = None

    maximum_value: str | None = None

    minimum_length: int | None = None

    maximum_length: int | None = None

    regex_pattern: str | None = None

    validation_message: str | None = None

    unit: str | None = None

    formula_reference: str | None = None

    is_active: bool = True


class SpecificationFieldCreate(
    SpecificationFieldBase
):
    """
    Create Specification Field.
    """

    pass


class SpecificationFieldUpdate(BaseModel):
    """
    Update Specification Field.
    """

    field_code: str | None = None

    field_name_en: str | None = None

    field_name_bn: str | None = None

    description: str | None = None

    group_id: int | None = None

    data_type: str | None = None

    input_control: str | None = None

    placeholder_en: str | None = None

    placeholder_bn: str | None = None

    default_value: str | None = None

    help_text: str | None = None

    icon: str | None = None

    is_required: bool | None = None

    is_editable: bool | None = None

    is_visible: bool | None = None

    is_calculated: bool | None = None

    is_system_field: bool | None = None

    display_order: int | None = None

    width: int | None = None

    minimum_value: str | None = None

    maximum_value: str | None = None

    minimum_length: int | None = None

    maximum_length: int | None = None

    regex_pattern: str | None = None

    validation_message: str | None = None

    unit: str | None = None

    formula_reference: str | None = None

    is_active: bool | None = None


class SpecificationFieldResponse(
    SpecificationFieldBase
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