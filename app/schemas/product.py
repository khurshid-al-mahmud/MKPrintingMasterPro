"""
Product Pydantic Schemas.

Request and Response Models
for Product API.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class ProductBase(BaseModel):
    """
    Common Product Fields.
    """

    product_code: str
    product_name: str
    category_id: int
    printing_type: str
    unit: str


class ProductCreate(ProductBase):
    """
    Create Product Schema.
    """

    pass


class ProductUpdate(BaseModel):
    """
    Update Product Schema.
    """

    product_code: str | None = None
    product_name: str | None = None
    category_id: int | None = None
    printing_type: str | None = None
    unit: str | None = None


class ProductResponse(ProductBase):
    """
    Product Response Schema.
    """

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )