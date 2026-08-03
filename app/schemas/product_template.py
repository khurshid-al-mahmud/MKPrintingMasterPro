"""
Product Template Schemas.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class ProductTemplateBase(BaseModel):
    """
    Common Product Template Fields.
    """

    template_code: str
    template_name: str
    product_id: int
    description: str | None = None
    is_default: bool = False


class ProductTemplateCreate(ProductTemplateBase):
    """
    Create Product Template.
    """

    pass


class ProductTemplateUpdate(BaseModel):
    """
    Update Product Template.
    """

    template_code: str | None = None
    template_name: str | None = None
    product_id: int | None = None
    description: str | None = None
    is_default: bool | None = None


class ProductTemplateResponse(ProductTemplateBase):
    """
    Product Template Response.
    """

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )