"""
Machine Pydantic Schemas.

Request and Response Models
for Machine API.
"""

from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class MachineBase(BaseModel):
    """
    Common Machine Fields.
    """

    machine_code: str
    machine_name: str
    machine_type: str
    manufacturer: str | None = None
    model: str | None = None
    max_sheet_size: str | None = None
    max_print_width: float | None = None
    max_print_length: float | None = None
    color_capacity: int | None = None
    production_speed: int | None = None
    hourly_running_cost: float = 0
    remarks: str | None = None


class MachineCreate(MachineBase):
    """
    Create Machine Schema.
    """

    pass


class MachineUpdate(BaseModel):
    """
    Update Machine Schema.
    """

    machine_code: str | None = None
    machine_name: str | None = None
    machine_type: str | None = None
    manufacturer: str | None = None
    model: str | None = None
    max_sheet_size: str | None = None
    max_print_width: float | None = None
    max_print_length: float | None = None
    color_capacity: int | None = None
    production_speed: int | None = None
    hourly_running_cost: float | None = None
    remarks: str | None = None
    is_active: bool | None = None


class MachineResponse(MachineBase):
    """
    Machine Response Schema.
    """

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )