"""
Specification Group Schemas.

Used for creating, updating and returning
Specification Group master data.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SpecificationGroupBase(BaseModel):
    """
    Common fields for Specification Group.
    """

    group_code: str
    group_name: str
    template_id: int
    display_order: int = 1
    description: str | None = None
    is_active: bool = True


class SpecificationGroupCreate(SpecificationGroupBase):
    """
    Schema for creating Specification Group.
    """

    pass


class SpecificationGroupUpdate(BaseModel):
    """
    Schema for updating Specification Group.
    """

    group_code: str | None = None
    group_name: str | None = None
    template_id: int | None = None
    display_order: int | None = None
    description: str | None = None
    is_active: bool | None = None


class SpecificationGroupResponse(SpecificationGroupBase):
    """
    Response schema.
    """

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    created_at: datetime
    updated_at: datetime