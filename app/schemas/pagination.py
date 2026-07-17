"""
Pagination Schemas.

Reusable pagination models
for the entire ERP system.
"""

from pydantic import BaseModel, ConfigDict


class PaginationParams(BaseModel):
    """
    Pagination request parameters.
    """

    page: int = 1
    page_size: int = 20

    model_config = ConfigDict(
        from_attributes=True,
    )


class PaginationMeta(BaseModel):
    """
    Pagination metadata.
    """

    page: int
    page_size: int
    total_records: int







class PaginationResponse(BaseModel):
    """
    Standard pagination response.
    """

    total_pages: int
    has_previous: bool
    has_next: bool
    meta: PaginationMeta

    model_config = ConfigDict(
        from_attributes=True,
    )