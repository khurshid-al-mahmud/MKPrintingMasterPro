"""
MKPrintingMasterPro ERP

Production Operation Execution Status Schemas

Build-035
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductionOperationExecutionStatusBase(BaseModel):
    status_code: str
    status_name: str
    description: str | None = None
    display_order: int = 1
    is_active: bool = True


class ProductionOperationExecutionStatusCreate(
    ProductionOperationExecutionStatusBase
):
    pass


class ProductionOperationExecutionStatusUpdate(BaseModel):
    status_name: str | None = None
    description: str | None = None
    display_order: int | None = None
    is_active: bool | None = None


class ProductionOperationExecutionStatusResponse(
    ProductionOperationExecutionStatusBase
):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
