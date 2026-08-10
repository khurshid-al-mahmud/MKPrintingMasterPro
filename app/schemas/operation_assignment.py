"""
MKPrintingMasterPro ERP

Operation Assignment Schemas

Build-032
"""

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class OperationAssignmentBase(BaseModel):

    production_order_id: int
    operation_id: int


    # Build-040
    machine_id: int | None = None
    sequence_no: int = 1

    assigned_party_id: Optional[int] = None
    assigned_type: str = "Internal"

    status: str = "Pending"

    is_required: bool = True
    is_completed: bool = False

    planned_start_date: Optional[date] = None
    planned_end_date: Optional[date] = None

    instructions: Optional[str] = None
    remarks: Optional[str] = None


class OperationAssignmentCreate(OperationAssignmentBase):

    created_by: Optional[str] = None
    updated_by: Optional[str] = None


class OperationAssignmentUpdate(BaseModel):

    operation_id: Optional[int] = None


    # Build-040
    machine_id: Optional[int] = None
    sequence_no: Optional[int] = None

    assigned_party_id: Optional[int] = None
    assigned_type: Optional[str] = None

    status: Optional[str] = None

    is_required: Optional[bool] = None
    is_completed: Optional[bool] = None

    planned_start_date: Optional[date] = None
    planned_end_date: Optional[date] = None

    instructions: Optional[str] = None
    remarks: Optional[str] = None

    updated_by: Optional[str] = None


class OperationAssignmentResponse(OperationAssignmentBase):

    id: int

    created_by: Optional[str] = None
    updated_by: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )