"""
Customer Pydantic Schemas.

Request and Response Models
for Customer API.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class CustomerBase(BaseModel):
    """
    Common Customer Fields.
    """

    party_id: int
    customer_number: str
    customer_category: str | None = None
    credit_limit: float = 0
    credit_days: int = 0
    price_category: str | None = None
    discount_rate: float = 0


class CustomerCreate(CustomerBase):
    """
    Create Customer Schema.
    """

    pass


class CustomerUpdate(BaseModel):
    """
    Update Customer Schema.
    """

    party_id: int | None = None
    customer_number: str | None = None
    customer_category: str | None = None
    credit_limit: float | None = None
    credit_days: int | None = None
    price_category: str | None = None
    discount_rate: float | None = None


class CustomerResponse(CustomerBase):
    """
    Customer Response Schema.
    """

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )