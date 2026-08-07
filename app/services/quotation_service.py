"""
Quotation Service.

Business Logic Layer
for Quotation Management.
"""

from app.models.quotation_master import QuotationMaster
from app.models.quotation_item import QuotationItem

from app.repositories.quotation_repository import (
    QuotationRepository,
)

from app.schemas.quotation import (
    QuotationCreate,
    QuotationUpdate,
)


class QuotationService:
    """
    Service layer for Quotation Management.
    """

    def __init__(
        self,
        repository: QuotationRepository,
        date_time_service,
    ) -> None:

        self.repository = repository
        self.date_time_service = date_time_service


    # ======================================
    # CREATE
    # ======================================

    def create(
        self,
        quotation: QuotationCreate,
    ) -> QuotationMaster:

        if self.repository.exists_by_quotation_no(
            quotation.quotation_no,
        ):
            raise ValueError(
                "Quotation number already exists.",
            )


        quotation_date = (
            self.date_time_service
            .get_document_date(
                quotation.quotation_date,
            )
        )


        subtotal = 0.0


        for item in quotation.items:

            item.amount = (
                item.quantity
                * item.unit_price
            )

            subtotal += item.amount


        discount = (
            quotation.discount_amount
            if quotation.discount_amount
            else 0
        )


        vat = (
            quotation.vat_amount
            if quotation.vat_amount
            else 0
        )


        tax = (
            quotation.tax_amount
            if quotation.tax_amount
            else 0
        )


        grand_total = (
            subtotal
            - discount
            + vat
            + tax
        )


        new_quotation = QuotationMaster(

            quotation_no=quotation.quotation_no,

            quotation_date=quotation_date,

            customer_id=quotation.customer_id,

            contact_person=quotation.contact_person,

            validity_days=quotation.validity_days,

            status=quotation.status,

            remarks=quotation.remarks,

            subtotal=subtotal,

            discount_amount=discount,

            vat_amount=vat,

            tax_amount=tax,

            grand_total=grand_total,
        )


        for item in quotation.items:

            new_item = QuotationItem(

                product_id=item.product_id,

                description=item.description,

                quantity=item.quantity,

                unit=item.unit,

                unit_price=item.unit_price,

                amount=item.amount,

                specification=item.specification,

                remarks=item.remarks,
            )


            new_quotation.items.append(
                new_item
            )


        return self.repository.create(
            new_quotation,
        )


    # ======================================
    # GET ALL
    # ======================================

    def get_all(
        self,
    ) -> list[QuotationMaster]:

        return self.repository.get_all()



    # ======================================
    # GET BY ID
    # ======================================

    def get_by_id(
        self,
        quotation_id: int,
    ) -> QuotationMaster | None:

        return self.repository.get_by_id(
            quotation_id,
        )



    # ======================================
    # UPDATE
    # ======================================

    def update(
        self,
        quotation_id: int,
        quotation_data: QuotationUpdate,
    ) -> QuotationMaster | None:


        update_data = quotation_data.model_dump(
            exclude_unset=True,
        )


        print(
            "UPDATE DATA:",
            update_data,
        )


        return self.repository.update(
            quotation_id,
            update_data,
        )



    # ======================================
    # DELETE
    # ======================================

    def delete(
        self,
        quotation_id: int,
    ) -> bool:

        return self.repository.delete(
            quotation_id,
        )