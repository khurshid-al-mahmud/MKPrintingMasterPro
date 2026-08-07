"""
MKPrintingMasterPro ERP

Production Output Schemas

Build-034
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


# ==========================
# Base Schema
# ==========================

class ProductionOutputBase(BaseModel):
    """
    Common fields for Production Output.
    """

    production_operation_execution_id: int

    output_quantity: float

    reject_quantity: float | None = 0

    output_status: str = "Completed"

    operator_name: str | None = None

    remarks: str | None = None


# ==========================
# Create Schema
# ==========================

class ProductionOutputCreate(ProductionOutputBase):
    """
    Schema for creating Production Output.
    """

    pass


# ==========================
# Update Schema
# ==========================

class ProductionOutputUpdate(BaseModel):
    """
    Schema for updating Production Output.
    """

    output_quantity: float | None = None

    reject_quantity: float | None = None

    output_status: str | None = None

    operator_name: str | None = None

    remarks: str | None = None


# ==========================
# Response Schema
# ==========================

class ProductionOutputResponse(ProductionOutputBase):
    """
    Response schema.
    """

    id: int

    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )