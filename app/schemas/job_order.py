"""
MKPrintingMasterPro ERP

Job Order Schema

Build-030
"""

from datetime import date
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


# ===========================
# Item
# ===========================

class JobOrderItemBase(BaseModel):

    product_id: int

    description: str

    quantity: float

    unit: str

    specification: str | None = None

    remarks: str | None = None


class JobOrderItemCreate(JobOrderItemBase):
    pass


class JobOrderItemResponse(JobOrderItemBase):

    id: int

    job_order_id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


# ===========================
# Master
# ===========================

class JobOrderBase(BaseModel):

    invoice_id: int

    quotation_id: int | None = None

    customer_id: int

    priority: str = "Normal"

    delivery_date: date | None = None

    remarks: str | None = None


class JobOrderCreate(JobOrderBase):

    items: list[JobOrderItemCreate]


class JobOrderResponse(JobOrderBase):

    id: int

    job_order_no: str

    job_order_date: datetime

    status: str

    created_at: datetime

    updated_at: datetime

    items: list[JobOrderItemResponse] = []

    model_config = ConfigDict(
        from_attributes=True,
    )