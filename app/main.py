import logging

import app.models

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request

from app.api import binding_type
from app.api import company_profile
from app.api import customer
from app.api import employee
from app.api import machine
from app.api import paper_brand
from app.api import paper_gsm
from app.api import paper_size
from app.api import paper_type
from app.api import party
from app.api import print_partner
from app.api import product
from app.api import product_category
from app.api import product_template
from app.api import supplier
from app.api import system_setting
from app.api import specification_group
from app.api import specification_field

logging.basicConfig(
    level=logging.DEBUG,
)

app = FastAPI(
    title="MKPrintingMasterPro ERP",
    version="0.1.0",
)


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    logging.exception(exc)

    return JSONResponse(
        status_code=500,
        content={
            "detail": str(exc),
        },
    )


@app.get("/")
def root():
    return {
        "message": "MKPrintingMasterPro ERP API is running",
    }


# ===========================
# Master Modules
# ===========================

app.include_router(party.router)
app.include_router(supplier.router)
app.include_router(customer.router)
app.include_router(employee.router)
app.include_router(print_partner.router)
app.include_router(product.router)
app.include_router(product_category.router)
app.include_router(product_template.router)
app.include_router(machine.router)
app.include_router(company_profile.router)
app.include_router(system_setting.router)
app.include_router(paper_type.router)
app.include_router(paper_brand.router)
app.include_router(paper_gsm.router)
app.include_router(paper_size.router)
app.include_router(binding_type.router)
app.include_router(specification_group.router)
app.include_router(specification_field.router)