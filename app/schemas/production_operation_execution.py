"""
MKPrintingMasterPro ERP

Production Operation Execution Schema

Build-033
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductionOperationExecutionBase(BaseModel):
    """
    Common fields.
    """

    production_order_id: int

    operation_assignment_id: int


    # Build-040
    machine_id: int | None = None
    status: str = "Pending"

    planned_quantity: float | None = None

    completed_quantity: float | None = 0

    reject_quantity: float | None = 0

    actual_start_time: datetime | None = None

    actual_end_time: datetime | None = None

    operator_name: str | None = None

    remarks: str | None = None



class ProductionOperationExecutionCreate(
    ProductionOperationExecutionBase
):
    """
    Create schema.
    """

    pass



class ProductionOperationExecutionUpdate(BaseModel):
    """
    Update schema.
    """

    # Build-040
    # Physical machine responsible for this operation.
    machine_id: int | None = None
    status: str | None = None

    completed_quantity: float | None = None

    reject_quantity: float | None = None

    actual_start_time: datetime | None = None

    actual_end_time: datetime | None = None

    operator_name: str | None = None

    remarks: str | None = None



class ProductionOperationExecutionResponse(
    ProductionOperationExecutionBase
):
    """
    Response schema.
    """

    id: int

    created_at: datetime

    updated_at: datetime


    model_config = ConfigDict(
        from_attributes=True
    )
