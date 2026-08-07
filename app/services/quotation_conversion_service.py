"""
MKPrintingMasterPro ERP

Quotation Conversion Service

Build-029

Quotation -> Invoice Conversion
"""

from app.models.invoice_master import InvoiceMaster
from app.models.invoice_item import InvoiceItem


class QuotationConversionService:
    """
    Convert Quotation into Invoice.
    """

    def __init__(
        self,
        quotation_repository,
        invoice_repository,
        numbering_service,
    ):
        self.quotation_repository = quotation_repository
        self.invoice_repository = invoice_repository
        self.numbering_service = numbering_service

    # ==========================================
    # Convert
    # ==========================================

    def convert(
        self,
        quotation_id: int,
    ):

        quotation = self.quotation_repository.get_by_id(
            quotation_id
        )

        if quotation is None:
            raise ValueError(
                "Quotation not found."
            )

        if quotation.status == "Converted":
            raise ValueError(
                "Quotation already converted."
            )

        invoice_no = (
            self.numbering_service.generate_next_number(
                "INV"
            )
        )

        invoice = InvoiceMaster(

            invoice_no=invoice_no,

            invoice_date=quotation.quotation_date,

            customer_id=quotation.customer_id,

            quotation_id=quotation.id,

            remarks=quotation.remarks,

            subtotal=float(quotation.subtotal),

            discount_amount=float(
                quotation.discount_amount
            ),

            vat_amount=float(
                quotation.vat_amount
            ),

            tax_amount=float(
                quotation.tax_amount
            ),

            grand_total=float(
                quotation.grand_total
            ),

            status="Draft",
        )

        for item in quotation.items:

            invoice_item = InvoiceItem(

                product_id=item.product_id,

                description=item.description,

                quantity=item.quantity,

                unit=item.unit,

                unit_price=item.unit_price,

                amount=item.amount,

                specification=item.specification,

                remarks=item.remarks,
            )

            invoice.items.append(
                invoice_item
            )

        invoice = self.invoice_repository.create(
            invoice
        )

        self.quotation_repository.update(
            quotation.id,
            {
                "status": "Converted",
            },
        )

        return invoice