"""
Invoice Schemas.
"""

from datetime import datetime

from pydantic import BaseModel

from app.schemas.invoice_item import (
    InvoiceItemResponse,
)


class InvoiceBase(BaseModel):

    invoice_no: str

    invoice_date: datetime

    customer_id: int

    quotation_id: int | None = None

    status: str = "Draft"

    remarks: str | None = None


    subtotal: float = 0

    discount_amount: float = 0

    vat_amount: float = 0

    tax_amount: float = 0

    grand_total: float = 0



class InvoiceCreate(
    InvoiceBase
):
    pass



class InvoiceUpdate(
    BaseModel
):

    invoice_no: str | None = None

    invoice_date: datetime | None = None

    customer_id: int | None = None

    quotation_id: int | None = None

    status: str | None = None

    remarks: str | None = None


    subtotal: float | None = None

    discount_amount: float | None = None

    vat_amount: float | None = None

    tax_amount: float | None = None

    grand_total: float | None = None



class InvoiceResponse(
    InvoiceBase
):

    id: int

    created_at: datetime

    updated_at: datetime


    items: list[InvoiceItemResponse] = []


    class Config:

        from_attributes = True