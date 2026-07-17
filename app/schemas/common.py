"""
Common Pydantic Schemas.

Reusable schemas
for the entire ERP system.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TimestampSchema(BaseModel):
    """
    Common timestamp fields.
    """

    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )


class ActiveStatusSchema(BaseModel):
    """
    Common active status field.
    """

    is_active: bool

    model_config = ConfigDict(
        from_attributes=True,
    )







class IdSchema(BaseModel):
    """
    Common ID field.
    """

    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )


class BaseResponseSchema(
    IdSchema,
    ActiveStatusSchema,
    TimestampSchema,
):
    """
    Standard response schema
    for all ERP modules.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )