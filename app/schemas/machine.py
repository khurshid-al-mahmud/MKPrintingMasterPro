"""
Machine Schema

Build-012
"""

from datetime import date
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel
from pydantic import ConfigDict


class MachineBase(BaseModel):
    machine_code: str
    machine_name: str
    machine_type: str

    manufacturer: str | None = None
    model: str | None = None

    serial_number: str | None = None
    asset_number: str | None = None

    machine_location: str | None = None
    operator_name: str | None = None

    max_paper_width: Decimal | None = None
    max_paper_height: Decimal | None = None

    minimum_gsm: int | None = None
    maximum_gsm: int | None = None

    color_capacity: int | None = None

    printing_speed: int | None = None

    hourly_running_cost: Decimal = Decimal("0.00")

    electric_consumption_kw: Decimal | None = None

    purchase_date: date | None = None
    installation_date: date | None = None

    last_maintenance_date: date | None = None
    next_maintenance_date: date | None = None

    status: str = "Running"

    remarks: str | None = None

    is_active: bool = True


class MachineCreate(MachineBase):
    pass


class MachineUpdate(BaseModel):
    machine_name: str | None = None
    machine_type: str | None = None

    manufacturer: str | None = None
    model: str | None = None

    serial_number: str | None = None
    asset_number: str | None = None

    machine_location: str | None = None
    operator_name: str | None = None

    max_paper_width: Decimal | None = None
    max_paper_height: Decimal | None = None

    minimum_gsm: int | None = None
    maximum_gsm: int | None = None

    color_capacity: int | None = None

    printing_speed: int | None = None

    hourly_running_cost: Decimal | None = None

    electric_consumption_kw: Decimal | None = None

    purchase_date: date | None = None
    installation_date: date | None = None

    last_maintenance_date: date | None = None
    next_maintenance_date: date | None = None

    status: str | None = None

    remarks: str | None = None

    is_active: bool | None = None


class MachineResponse(MachineBase):
    id: int

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )