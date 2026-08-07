"""
Invoice Item Service.

Business logic layer
for Invoice Item Management.
"""

from app.repositories.invoice_item_repository import (
    InvoiceItemRepository,
)

from app.repositories.invoice_repository import (
    InvoiceRepository,
)

from app.models.invoice_item import (
    InvoiceItem,
)


class InvoiceItemService:
    """
    Invoice Item Service.
    """

    def __init__(
        self,
        invoice_item_repository: InvoiceItemRepository,
        invoice_repository: InvoiceRepository,
    ):
        self.invoice_item_repository = invoice_item_repository
        self.invoice_repository = invoice_repository

    # ======================================
    # GET ALL
    # ======================================

    def get_all(self):

        return self.invoice_item_repository.get_all()

    # ======================================
    # GET BY ID
    # ======================================

    def get_by_id(
        self,
        item_id: int,
    ):

        return self.invoice_item_repository.get_by_id(
            item_id
        )

    # ======================================
    # CREATE
    # ======================================

    def create(
        self,
        item_data,
    ):

        item_data["amount"] = (
            item_data.get("quantity", 0)
            * item_data.get("unit_price", 0)
        )

        item = InvoiceItem(
            **item_data
        )

        result = self.invoice_item_repository.create(
            item
        )

        self.invoice_repository.update_invoice_total(
            item.invoice_id
        )

        return result

    # ======================================
    # UPDATE
    # ======================================

    def update(
        self,
        item_id: int,
        item_data,
    ):

        item = self.invoice_item_repository.get_by_id(
            item_id
        )

        if item is None:
            return None

        quantity = item_data.get(
            "quantity",
            item.quantity,
        )

        unit_price = item_data.get(
            "unit_price",
            item.unit_price,
        )

        item_data["amount"] = (
            quantity * unit_price
        )

        for key, value in item_data.items():

            setattr(
                item,
                key,
                value,
            )

        self.invoice_item_repository.update()

        self.invoice_repository.update_invoice_total(
            item.invoice_id
        )

        return item

    # ======================================
    # DELETE
    # ======================================

    def delete(
        self,
        item_id: int,
    ):

        item = self.invoice_item_repository.get_by_id(
            item_id
        )

        if item is None:
            return False

        invoice_id = item.invoice_id

        self.invoice_item_repository.delete(
            item
        )

        self.invoice_repository.update_invoice_total(
            invoice_id
        )

        return True