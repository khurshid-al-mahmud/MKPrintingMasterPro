"""
Paper GSM Schemas.

Pydantic schemas for
Paper GSM Master.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class PaperGSMBase(BaseModel):
    """Base Paper GSM Schema."""

    gsm_code: str = Field(
        ...,
        max_length=30,
    )

    gsm_name: str = Field(
        ...,
        max_length=100,
    )

    gsm_value: float = Field(
        ...,
        gt=0,
    )

    paper_category: str | None = Field(
        default=None,
        max_length=100,
    )

    display_order: int = Field(
        default=1,
        ge=1,
    )

    is_active: bool = True


class PaperGSMCreate(PaperGSMBase):
    """Create Paper GSM Schema."""

    pass


class PaperGSMUpdate(BaseModel):
    """Update Paper GSM Schema."""

    gsm_code: str | None = Field(
        default=None,
        max_length=30,
    )

    gsm_name: str | None = Field(
        default=None,
        max_length=100,
    )

    gsm_value: float | None = Field(
        default=None,
        gt=0,
    )

    paper_category: str | None = Field(
        default=None,
        max_length=100,
    )

    display_order: int | None = Field(
        default=None,
        ge=1,
    )

    is_active: bool | None = None


class PaperGSMResponse(PaperGSMBase):
    """Paper GSM Response Schema."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    created_at: datetime

    updated_at: datetime