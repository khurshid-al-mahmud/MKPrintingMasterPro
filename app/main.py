from fastapi import FastAPI

from app.api import customer
from app.api import employee
from app.api import machine
from app.api import paper_brand
from app.api import paper_gsm
from app.api import paper_type
from app.api import party
from app.api import print_partner
from app.api import product
from app.api import supplier

app = FastAPI(
    title="MKPrintingMasterPro ERP",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "MKPrintingMasterPro ERP API is running",
    }


app.include_router(
    party.router,
)

app.include_router(
    supplier.router,
)

app.include_router(
    customer.router,
)

app.include_router(
    employee.router,
)

app.include_router(
    print_partner.router,
)

app.include_router(
    machine.router,
)

app.include_router(
    product.router,
)

app.include_router(
    paper_type.router,
)

app.include_router(
    paper_brand.router,
)

app.include_router(
    paper_gsm.router,
)