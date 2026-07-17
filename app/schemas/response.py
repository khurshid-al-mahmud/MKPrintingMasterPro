"""
Standard API Response Schemas.

Reusable response models
for the entire ERP system.
"""

from typing import Any

from pydantic import BaseModel, ConfigDict


class ApiResponse(BaseModel):
    """
    Standard API response.
    """

    success: bool
    message: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class DataResponse(ApiResponse):
    """
    API response with data.
    """

    data: Any | None = None







class ListResponse(ApiResponse):
    """
    API response for list data.
    """

    data: list[Any] = []

    total: int = 0

    model_config = ConfigDict(
        from_attributes=True,
    )


class ErrorResponse(ApiResponse):
    """
    Standard error response.
    """

    error_code: str | None = None

    details: Any | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )