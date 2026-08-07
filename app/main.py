"""
MKPrintingMasterPro ERP

Application Main Entry

Build-034
"""

from fastapi import FastAPI

from app.api import (
    company_profile,
    customer,
    employee,
    field_option,
    formula_rule,
    invoice,
    invoice_item,
    job_order,
    job_order_status_history,
    machine,
    operation_assignment,
    operation_master,
    paper_brand,
    paper_gsm,
    paper_size,
    paper_type,
    party,
    print_partner,
    production_operation_execution,
    production_output,
    production_order,
    product,
    product_category,
    product_template,
    quotation,
    quotation_item,
    specification_dependency_rule,
    specification_field,
    specification_group,
    supplier,
    system_setting,
    template_field_mapping,
    validation_rule,
)


app = FastAPI(
    title="MKPrintingMasterPro ERP",
    version="Build-034",
    description="Printing ERP Management System",
)


# ==========================
# Company / Party Master
# ==========================

app.include_router(company_profile.router)
app.include_router(customer.router)
app.include_router(employee.router)
app.include_router(machine.router)
app.include_router(party.router)
app.include_router(supplier.router)
app.include_router(print_partner.router)
app.include_router(system_setting.router)


# ==========================
# Product & Specification
# ==========================

app.include_router(product.router)
app.include_router(product_category.router)
app.include_router(product_template.router)

app.include_router(specification_group.router)
app.include_router(specification_field.router)
app.include_router(field_option.router)

app.include_router(validation_rule.router)
app.include_router(formula_rule.router)

app.include_router(
    specification_dependency_rule.router
)

app.include_router(
    template_field_mapping.router
)


# ==========================
# Paper Master
# ==========================

app.include_router(paper_brand.router)
app.include_router(paper_type.router)
app.include_router(paper_size.router)
app.include_router(paper_gsm.router)


# ==========================
# Sales
# ==========================

app.include_router(quotation.router)
app.include_router(quotation_item.router)

app.include_router(invoice.router)
app.include_router(invoice_item.router)


# ==========================
# Job Order
# ==========================

app.include_router(job_order.router)

app.include_router(
    job_order_status_history.router
)


# ==========================
# Production
# Build-031 / Build-034
# ==========================

app.include_router(
    production_order.router
)

app.include_router(
    operation_master.router
)

app.include_router(
    operation_assignment.router
)


# Build-033
# Production Operation Execution API

app.include_router(
    production_operation_execution.router
)


# Build-034
# Production Output API

app.include_router(
    production_output.router
)


# ==========================
# Root API
# ==========================

@app.get("/")
def root():
    return {
        "application": "MKPrintingMasterPro ERP",
        "version": "Build-034",
        "status": "Running"
    }