"""
MKPrintingMasterPro ERP

Operation Master Schemas

Build-031
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# ==========================================================
# Create
# ==========================================================

class OperationMasterCreate(BaseModel):
    """
    Schema for creating an Operation Master.
    """

    operation_code: str = Field(
        min_length=1,
        max_length=50,
    )

    operation_name: str = Field(
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
    )

    display_order: int = Field(
        default=1,
        ge=1,
    )

    is_active: bool = True

    created_by: str | None = Field(
        default=None,
        max_length=100,
    )

    updated_by: str | None = Field(
        default=None,
        max_length=100,
    )


# ==========================================================
# Update
# ==========================================================

class OperationMasterUpdate(BaseModel):
    """
    Schema for updating an Operation Master.
    """

    operation_code: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
    )

    operation_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=2000,
    )

    display_order: int | None = Field(
        default=None,
        ge=1,
    )

    is_active: bool | None = None

    updated_by: str | None = Field(
        default=None,
        max_length=100,
    )


# ==========================================================
# Response
# ==========================================================

class OperationMasterResponse(BaseModel):
    """
    API response schema for Operation Master.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    operation_code: str

    operation_name: str

    description: str | None

    display_order: int

    is_active: bool

    created_by: str | None

    updated_by: str | None

    created_at: datetime

    updated_at: datetime