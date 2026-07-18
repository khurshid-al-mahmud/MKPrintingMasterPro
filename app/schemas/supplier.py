"""
Supplier Pydantic Schemas.

Request and Response Models
for Supplier API.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class SupplierBase(BaseModel):
    """
    Common Supplier Fields.
    """

    party_id: int
    supplier_code: str
    trade_license: str | None = None
    vat_number: str | None = None
    tin_number: str | None = None
    credit_limit: float = 0
    current_balance: float = 0


class SupplierCreate(SupplierBase):
    """
    Create Supplier Schema.
    """

    pass


class SupplierUpdate(BaseModel):
    """
    Update Supplier Schema.
    """

    party_id: int | None = None
    supplier_code: str | None = None
    trade_license: str | None = None
    vat_number: str | None = None
    tin_number: str | None = None
    credit_limit: float | None = None
    current_balance: float | None = None


class SupplierResponse(SupplierBase):
    """
    Supplier Response Schema.
    """

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )