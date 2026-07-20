"""
Paper Size Schemas.

Pydantic schemas for
Paper Size Master.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class PaperSizeBase(BaseModel):
    """Shared Paper Size fields."""

    paper_size_code: str
    paper_size_name: str
    width_mm: int
    height_mm: int
    display_order: int = 1
    is_active: bool = True


class PaperSizeCreate(PaperSizeBase):
    """Schema for creating Paper Size."""
    pass


class PaperSizeUpdate(BaseModel):
    """Schema for updating Paper Size."""

    paper_size_code: str | None = None
    paper_size_name: str | None = None
    width_mm: int | None = None
    height_mm: int | None = None
    display_order: int | None = None
    is_active: bool | None = None


class PaperSizeResponse(PaperSizeBase):
    """Schema returned from database."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime