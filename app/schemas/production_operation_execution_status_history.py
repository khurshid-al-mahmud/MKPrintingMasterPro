"""
MKPrintingMasterPro ERP

Production Operation Execution Status History Schemas

Build-035
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductionOperationExecutionStatusHistoryResponse(BaseModel):
    """
    Response schema for Production Operation Execution Status History.
    """

    id: int

    production_operation_execution_id: int

    previous_status: str | None

    new_status: str

    completed_quantity: float | None

    reject_quantity: float | None

    operator_name: str | None

    remarks: str | None

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )