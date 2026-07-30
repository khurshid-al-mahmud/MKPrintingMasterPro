"""
Product Category Schemas.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductCategoryBase(BaseModel):
    category_code: str
    category_name: str
    description: str | None = None
    sort_order: int = 1


class ProductCategoryCreate(ProductCategoryBase):
    pass


class ProductCategoryUpdate(BaseModel):
    category_code: str | None = None
    category_name: str | None = None
    description: str | None = None
    sort_order: int | None = None
    is_active: bool | None = None


class ProductCategoryResponse(ProductCategoryBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )