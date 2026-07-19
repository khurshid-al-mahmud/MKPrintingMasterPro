"""
Paper Brand Schemas.

Pydantic schemas for
Paper Brand Master.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class PaperBrandBase(BaseModel):
    """Base Paper Brand Schema."""

    brand_code: str = Field(
        ...,
        max_length=30,
    )

    brand_name: str = Field(
        ...,
        max_length=150,
    )

    manufacturer: str | None = Field(
        default=None,
        max_length=150,
    )

    country: str | None = Field(
        default=None,
        max_length=100,
    )

    display_order: int = Field(
        default=1,
        ge=1,
    )

    is_active: bool = True


class PaperBrandCreate(PaperBrandBase):
    """Create Paper Brand Schema."""

    pass


class PaperBrandUpdate(BaseModel):
    """Update Paper Brand Schema."""

    brand_code: str | None = Field(
        default=None,
        max_length=30,
    )

    brand_name: str | None = Field(
        default=None,
        max_length=150,
    )

    manufacturer: str | None = Field(
        default=None,
        max_length=150,
    )

    country: str | None = Field(
        default=None,
        max_length=100,
    )

    display_order: int | None = Field(
        default=None,
        ge=1,
    )

    is_active: bool | None = None


class PaperBrandResponse(PaperBrandBase):
    """Paper Brand Response Schema."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    created_at: datetime

    updated_at: datetime