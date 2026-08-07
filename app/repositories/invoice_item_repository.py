"""
Invoice Item Repository.

Database operations
for Invoice Item.
"""

from sqlalchemy.orm import Session

from app.models.invoice_item import InvoiceItem


class InvoiceItemRepository:
    """Invoice Item Repository."""

    def __init__(
        self,
        db: Session,
    ):
        self.db = db


    def get_all(self):
        return (
            self.db.query(InvoiceItem)
            .all()
        )


    def get_by_id(
        self,
        item_id: int,
    ):
        return (
            self.db.query(InvoiceItem)
            .filter(
                InvoiceItem.id == item_id
            )
            .first()
        )


    def create(
        self,
        item: InvoiceItem,
    ):
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)

        return item


    def update(
        self,
    ):
        self.db.commit()


    def delete(
        self,
        item: InvoiceItem,
    ):
        self.db.delete(item)
        self.db.commit()