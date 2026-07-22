"""
Company Profile Schemas.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class CompanyProfileBase(BaseModel):
    company_name: str
    company_name_en: str | None = None

    logo_path: str | None = None

    address: str | None = None

    mobile: str | None = None

    phone: str | None = None

    email: str | None = None

    website: str | None = None

    facebook: str | None = None

    trade_license: str | None = None

    bin_number: str | None = None

    tin_number: str | None = None

    vat_number: str | None = None

    bank_name: str | None = None

    bank_account_name: str | None = None

    bank_account_number: str | None = None

    bank_branch: str | None = None

    confidential_visible: bool = False

    is_active: bool = True


class CompanyProfileCreate(CompanyProfileBase):
    pass


class CompanyProfileUpdate(BaseModel):
    company_name: str | None = None
    company_name_en: str | None = None

    logo_path: str | None = None

    address: str | None = None

    mobile: str | None = None

    phone: str | None = None

    email: str | None = None

    website: str | None = None

    facebook: str | None = None

    trade_license: str | None = None

    bin_number: str | None = None

    tin_number: str | None = None

    vat_number: str | None = None

    bank_name: str | None = None

    bank_account_name: str | None = None

    bank_account_number: str | None = None

    bank_branch: str | None = None

    confidential_visible: bool | None = None

    is_active: bool | None = None


class CompanyProfileResponse(CompanyProfileBase):
    model_config = ConfigDict(from_attributes=True)

    id: int

    created_at: datetime

    updated_at: datetime