"""
MKPrintingMasterPro ERP

FastAPI Application Main

Build-032
"""

from fastapi import FastAPI

from app.api import (
    company_profile,
    system_setting,
    machine,
    binding_type,
    party,
    operation_master,
    operation_assignment,
    production_order,
    job_order,
    job_order_status_history,
    quotation_conversion,
    specification_runtime,
)


app = FastAPI(
    title="MKPrintingMasterPro ERP",
    version="Build-032",
    description="Printing ERP Management System",
)


# ==========================
# API ROUTERS
# ==========================

app.include_router(
    company_profile.router
)

app.include_router(
    system_setting.router
)

app.include_router(
    machine.router
)

app.include_router(
    binding_type.router
)

app.include_router(
    party.router
)

app.include_router(
    operation_master.router
)

app.include_router(
    operation_assignment.router
)

app.include_router(
    production_order.router
)

app.include_router(
    job_order.router
)

app.include_router(
    job_order_status_history.router
)

app.include_router(
    quotation_conversion.router
)

app.include_router(
    specification_runtime.router
)


# ==========================
# ROOT TEST
# ==========================

@app.get("/")
def root():
    return {
        "app": "MKPrintingMasterPro ERP",
        "version": "Build-032",
        "status": "Running"
    }