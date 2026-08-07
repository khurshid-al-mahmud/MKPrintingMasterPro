"""
Invoice Service.

Business logic layer
for Invoice Management.
"""


from app.models.invoice_master import InvoiceMaster

from app.repositories.invoice_repository import (
    InvoiceRepository,
)



class InvoiceService:
    """
    Invoice Service.
    """


    def __init__(
        self,
        repository: InvoiceRepository,
    ):
        self.repository = repository



    # ======================================
    # CALCULATE TOTALS
    # Invoice Master Calculation
    # ======================================

    def calculate_totals(
        self,
        invoice: InvoiceMaster,
    ):

        subtotal = sum(
            item.amount
            for item in invoice.items
        )


        invoice.subtotal = subtotal


        invoice.grand_total = (
            subtotal
            - invoice.discount_amount
            + invoice.vat_amount
            + invoice.tax_amount
        )


        return invoice



    # ======================================
    # GET ALL
    # ======================================

    def get_all(self):

        return self.repository.get_all()



    # ======================================
    # GET BY ID
    # ======================================

    def get_by_id(
        self,
        invoice_id: int,
    ):

        return self.repository.get_by_id(
            invoice_id
        )



    # ======================================
    # CREATE
    # ======================================

    def create(
        self,
        invoice_data,
    ):

        invoice = InvoiceMaster(
            **invoice_data
        )


        self.calculate_totals(
            invoice
        )


        return self.repository.create(
            invoice
        )



    # ======================================
    # UPDATE
    # ======================================

    def update(
        self,
        invoice_id: int,
        invoice_data,
    ):

        invoice = self.repository.get_by_id(
            invoice_id
        )


        if invoice is None:
            return None



        for key, value in invoice_data.items():

            setattr(
                invoice,
                key,
                value,
            )



        self.calculate_totals(
            invoice
        )


        self.repository.update()


        return invoice



    # ======================================
    # DELETE
    # ======================================

    def delete(
        self,
        invoice_id: int,
    ):

        invoice = self.repository.get_by_id(
            invoice_id
        )


        if invoice is None:
            return False



        self.repository.delete(
            invoice
        )


        return True