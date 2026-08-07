"""
Quotation Item Service.

Business Logic Layer
for Quotation Item Management.
"""

from app.models.quotation_item import QuotationItem

from app.repositories.quotation_item_repository import (
    QuotationItemRepository,
)

from app.schemas.quotation_item import (
    QuotationItemCreate,
    QuotationItemUpdate,
)


class QuotationItemService:
    """
    Service layer for Quotation Item.
    """

    def __init__(
        self,
        repository: QuotationItemRepository,
    ) -> None:

        self.repository = repository



    def create(
        self,
        item: QuotationItemCreate,
    ) -> QuotationItem:
        """
        Create quotation item.
        """

        new_item = QuotationItem(

            quotation_id=item.quotation_id,

            product_id=item.product_id,

            description=item.description,

            quantity=item.quantity,

            unit=item.unit,

            unit_price=item.unit_price,

            amount=item.amount,

            specification=item.specification,

            remarks=item.remarks,
        )


        return self.repository.create(
            new_item
        )



    def get_all(
        self,
    ) -> list[QuotationItem]:
        """
        Get all quotation items.
        """

        return self.repository.get_all()



    def get_by_id(
        self,
        item_id: int,
    ) -> QuotationItem | None:
        """
        Get item by ID.
        """

        return self.repository.get_by_id(
            item_id
        )



    def update(
        self,
        item_id: int,
        item_data: QuotationItemUpdate,
    ) -> QuotationItem | None:
        """
        Update quotation item.
        """

        return self.repository.update(
            item_id,
            item_data.model_dump(
                exclude_unset=True
            ),
        )



    def delete(
        self,
        item_id: int,
    ) -> bool:
        """
        Delete quotation item.
        """

        return self.repository.delete(
            item_id
        )