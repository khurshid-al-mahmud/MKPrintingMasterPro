"""
Quotation Pydantic Schemas.

Request and Response Models
for Quotation API.
"""

from datetime import date, datetime

from pydantic import BaseModel
from pydantic import ConfigDict

from app.schemas.quotation_item import (
    QuotationItemNestedCreate,
    QuotationItemResponse,
)


class QuotationBase(BaseModel):
    """
    Common Quotation Fields.
    """

    quotation_no: str
    quotation_date: date | None = None
    customer_id: int

    contact_person: str | None = None
    validity_days: int | None = None
    status: str | None = None
    remarks: str | None = None

    subtotal: float | None = None
    discount_amount: float | None = None
    vat_amount: float | None = None
    tax_amount: float | None = None
    grand_total: float | None = None


class QuotationCreate(QuotationBase):
    """
    Create Quotation Schema.
    """

    items: list[QuotationItemNestedCreate] = []


class QuotationUpdate(BaseModel):
    """
    Update Quotation Schema.
    """

    quotation_no: str | None = None
    quotation_date: date | None = None
    customer_id: int | None = None

    contact_person: str | None = None
    validity_days: int | None = None
    status: str | None = None
    remarks: str | None = None

    subtotal: float | None = None
    discount_amount: float | None = None
    vat_amount: float | None = None
    tax_amount: float | None = None
    grand_total: float | None = None


class QuotationResponse(QuotationBase):
    """
    Quotation Response Schema.
    """

    id: int

    items: list["QuotationItemResponse"] = []

    created_by: str | None = None
    updated_by: str | None = None

    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )