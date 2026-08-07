"""
Quotation Item Schemas.

Request and Response Models
for Quotation Item.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class QuotationItemBase(BaseModel):
    """
    Common Quotation Item Fields.
    """

    quotation_id: int

    product_id: int

    description: str | None = None

    quantity: float
    unit: str | None = None

    unit_price: float
    amount: float | None = None

    specification: str | None = None
    remarks: str | None = None


class QuotationItemCreate(QuotationItemBase):
    """
    Create Quotation Item Schema.
    """

    pass


class QuotationItemNestedCreate(BaseModel):
    """
    Used when creating a quotation with items.
    """

    product_id: int

    description: str | None = None

    quantity: float
    unit: str | None = None

    unit_price: float
    amount: float | None = None

    specification: str | None = None
    remarks: str | None = None


class QuotationItemUpdate(BaseModel):
    """
    Update Quotation Item Schema.
    """

    quotation_id: int | None = None
    product_id: int | None = None

    description: str | None = None

    quantity: float | None = None
    unit: str | None = None

    unit_price: float | None = None
    amount: float | None = None

    specification: str | None = None
    remarks: str | None = None


class QuotationItemResponse(QuotationItemBase):
    """
    Quotation Item Response Schema.
    """

    id: int

    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )