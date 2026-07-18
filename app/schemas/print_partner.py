"""
Print Partner Pydantic Schemas.

Request and Response Models
for Print Partner API.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class PrintPartnerBase(BaseModel):
    """
    Common Print Partner Fields.
    """

    party_id: int
    partner_code: str
    specialization: str | None = None
    machine_type: str | None = None
    commission_rate: float = 0
    payment_terms: str | None = None


class PrintPartnerCreate(PrintPartnerBase):
    """
    Create Print Partner Schema.
    """

    pass


class PrintPartnerUpdate(BaseModel):
    """
    Update Print Partner Schema.
    """

    party_id: int | None = None
    partner_code: str | None = None
    specialization: str | None = None
    machine_type: str | None = None
    commission_rate: float | None = None
    payment_terms: str | None = None


class PrintPartnerResponse(PrintPartnerBase):
    """
    Print Partner Response Schema.
    """

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )