from fastapi import FastAPI

from app.api import customer, party, supplier

app = FastAPI(
    title="MKPrintingMasterPro ERP",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "MKPrintingMasterPro ERP API is running"
    }


# Party API
app.include_router(
    party.router,
)

# Supplier API
app.include_router(
    supplier.router,
)

# Customer API
app.include_router(
    customer.router,
)