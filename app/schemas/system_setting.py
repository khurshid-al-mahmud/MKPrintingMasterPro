"""
System Setting Schemas.

Pydantic schemas for System Setting Master CRUD.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# -----------------------------
# Base
# -----------------------------
class SystemSettingBase(BaseModel):
    setting_key: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["default_paper_size"],
    )

    setting_value: str | None = Field(
        default=None,
        examples=["A4"],
    )

    description: str | None = Field(
        default=None,
        max_length=255,
        examples=["Default paper size"],
    )

    is_active: bool = True


# -----------------------------
# Create
# -----------------------------
class SystemSettingCreate(SystemSettingBase):
    pass


# -----------------------------
# Update
# -----------------------------
class SystemSettingUpdate(BaseModel):
    setting_key: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    setting_value: str | None = None

    description: str | None = Field(
        default=None,
        max_length=255,
    )

    is_active: bool | None = None


# -----------------------------
# Response
# -----------------------------
class SystemSettingResponse(SystemSettingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)