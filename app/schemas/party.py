"""
Party Pydantic Schemas.

Request and Response Models
for Party API.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PartyBase(BaseModel):
    """Common Party Fields."""

    party_name: str
    mobile: str | None = None
    email: str | None = None
    address: str | None = None


class PartyCreate(PartyBase):
    """Schema for Create Party."""

    pass


class PartyUpdate(BaseModel):
    """Schema for Update Party."""

    party_name: str | None = None
    mobile: str | None = None
    email: str | None = None
    address: str | None = None




# ================= PART-2 HERE =================



class PartyResponse(PartyBase):
    """Schema for Party Response."""

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )