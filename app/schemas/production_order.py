"""
MKPrintingMasterPro ERP

Production Order Schemas

Build-031
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProductionOrderBase(BaseModel):

    production_order_no: str

    production_order_date: datetime

    job_order_id: int

    status: str = "Open"

    priority: str = "Normal"

    planned_start_date: datetime | None = None

    planned_end_date: datetime | None = None

    remarks: str | None = None


class ProductionOrderCreate(
    ProductionOrderBase
):
    created_by: str | None = None


class ProductionOrderUpdate(
    BaseModel
):

    production_order_date: datetime | None = None

    job_order_id: int | None = None

    status: str | None = None

    priority: str | None = None

    planned_start_date: datetime | None = None

    planned_end_date: datetime | None = None

    remarks: str | None = None

    updated_by: str | None = None


class ProductionOrderResponse(
    ProductionOrderBase
):

    id: int

    created_by: str | None = None

    updated_by: str | None = None

    created_at: datetime

    updated_at: datetime | None = None


    model_config = ConfigDict(
        from_attributes=True
    )