"""
Invoice Item Schemas.
"""

from datetime import datetime

from pydantic import BaseModel

from app.schemas.product import (
    ProductResponse,
)


class InvoiceItemBase(BaseModel):

    invoice_id: int

    product_id: int

    description: str

    quantity: float = 0

    unit: str

    unit_price: float = 0

    amount: float = 0

    specification: str | None = None

    remarks: str | None = None



class InvoiceItemCreate(
    InvoiceItemBase
):
    pass



class InvoiceItemUpdate(
    BaseModel
):

    product_id: int | None = None

    description: str | None = None

    quantity: float | None = None

    unit: str | None = None

    unit_price: float | None = None

    amount: float | None = None

    specification: str | None = None

    remarks: str | None = None



class InvoiceItemResponse(
    InvoiceItemBase
):

    id: int

    created_at: datetime

    updated_at: datetime

    product: ProductResponse | None = None


    class Config:
        from_attributes = True