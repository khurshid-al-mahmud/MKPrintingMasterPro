from fastapi import FastAPI

app = FastAPI(
    title="MKPrintingMasterPro ERP",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "MKPrintingMasterPro ERP API is running"
    }