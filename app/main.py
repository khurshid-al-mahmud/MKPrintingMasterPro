from fastapi import FastAPI

from app.api import customer
from app.api import employee
from app.api import party
from app.api import supplier
from app.api import print_partner


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