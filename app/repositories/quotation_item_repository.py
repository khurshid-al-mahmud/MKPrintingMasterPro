"""
Quotation Item Repository.

Database access layer
for Quotation Item Management.
"""

from app.models.quotation_item import QuotationItem


class QuotationItemRepository:
    """
    Repository for Quotation Item.
    """

    def __init__(
        self,
        db,
    ):
        self.db = db


    def create(
        self,
        item: QuotationItem,
    ) -> QuotationItem:

        self.db.add(item)

        self.db.commit()

        self.db.refresh(item)

        return item



    def get_by_id(
        self,
        item_id: int,
    ) -> QuotationItem | None:

        return (
            self.db.query(QuotationItem)
            .filter(
                QuotationItem.id == item_id,
            )
            .first()
        )



    def get_all(
        self,
    ) -> list[QuotationItem]:

        return (
            self.db.query(QuotationItem)
            .all()
        )



    def update(
        self,
        item_id: int,
        item_data: dict,
    ) -> QuotationItem | None:

        item = self.get_by_id(item_id)

        if item is None:
            return None


        for key, value in item_data.items():

            setattr(
                item,
                key,
                value,
            )


        self.db.commit()

        self.db.refresh(item)

        return item



    def delete(
        self,
        item_id: int,
    ) -> bool:

        item = self.get_by_id(item_id)

        if item is None:
            return False


        self.db.delete(item)

        self.db.commit()

        return True