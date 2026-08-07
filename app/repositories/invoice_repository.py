"""
Invoice Repository.

Database operations
for Invoice Master.
"""

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.models.invoice_master import InvoiceMaster
from app.models.invoice_item import InvoiceItem


class InvoiceRepository:
    """Invoice Repository."""

    def __init__(
        self,
        db: Session,
    ):
        self.db = db


    # ======================================
    # GET ALL
    # ======================================

    def get_all(self):

        return (
            self.db.query(InvoiceMaster)
            .options(
                joinedload(
                    InvoiceMaster.customer
                ),
                joinedload(
                    InvoiceMaster.items
                ).joinedload(
                    InvoiceItem.product
                ),
            )
            .all()
        )


    # ======================================
    # GET BY ID
    # ======================================

    def get_by_id(
        self,
        invoice_id: int,
    ):

        return (
            self.db.query(InvoiceMaster)
            .options(
                joinedload(
                    InvoiceMaster.customer
                ),
                joinedload(
                    InvoiceMaster.items
                ).joinedload(
                    InvoiceItem.product
                ),
            )
            .filter(
                InvoiceMaster.id == invoice_id
            )
            .first()
        )


    # ======================================
    # CREATE
    # ======================================

    def create(
        self,
        invoice: InvoiceMaster,
    ):

        self.db.add(invoice)

        self.db.commit()

        self.db.refresh(invoice)

        return invoice


    # ======================================
    # UPDATE
    # ======================================

    def update(self):

        self.db.commit()



    # ======================================
    # RECALCULATE TOTAL
    # ======================================

    def update_invoice_total(
        self,
        invoice_id: int,
    ):

        invoice = self.get_by_id(
            invoice_id
        )


        if invoice is None:
            return None



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


        self.db.commit()

        self.db.refresh(invoice)


        return invoice



    # ======================================
    # DELETE
    # ======================================

    def delete(
        self,
        invoice: InvoiceMaster,
    ):

        self.db.delete(invoice)

        self.db.commit()