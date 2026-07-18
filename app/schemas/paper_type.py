"""
Paper Type Master Schemas.

Used by:

- Create
- Update
- Response
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class PaperTypeBase(BaseModel):
    """Base schema for Paper Type."""

    paper_type_code: str = Field(
        ...,
        min_length=1,
        max_length=30,
    )

    paper_type_name: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )

    display_order: int = Field(
        default=1,
        ge=1,
    )

    remarks: str | None = Field(
        default=None,
        max_length=5000,
    )

    is_active: bool = True


class PaperTypeCreate(PaperTypeBase):
    """Schema for creating Paper Type."""


class PaperTypeUpdate(BaseModel):
    """Schema for updating Paper Type."""

    paper_type_code: str | None = Field(
        default=None,
        min_length=1,
        max_length=30,
    )

    paper_type_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    display_order: int | None = Field(
        default=None,
        ge=1,
    )

    remarks: str | None = Field(
        default=None,
        max_length=5000,
    )

    is_active: bool | None = None


class PaperTypeResponse(PaperTypeBase):
    """Response schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int

    created_at: datetime

    updated_at: datetime