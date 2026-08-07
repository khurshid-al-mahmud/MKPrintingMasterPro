"""
Quotation Repository.

Database access layer
for Quotation Management.
"""

from sqlalchemy.orm import selectinload

from app.models.quotation_master import QuotationMaster


class QuotationRepository:
    """
    Repository for Quotation.
    """

    def __init__(
        self,
        db,
    ):
        self.db = db


    def create(
        self,
        quotation: QuotationMaster,
    ) -> QuotationMaster:

        self.db.add(quotation)

        self.db.commit()

        self.db.refresh(quotation)

        return quotation


    def get_by_id(
        self,
        quotation_id: int,
    ) -> QuotationMaster | None:

        return (
            self.db.query(QuotationMaster)
            .options(
                selectinload(
                    QuotationMaster.items
                )
            )
            .filter(
                QuotationMaster.id == quotation_id,
            )
            .first()
        )


    def get_all(
        self,
    ) -> list[QuotationMaster]:

        return (
            self.db.query(QuotationMaster)
            .options(
                selectinload(
                    QuotationMaster.items
                )
            )
            .order_by(
                QuotationMaster.id.desc()
            )
            .all()
        )


    def update(
        self,
        quotation_id: int,
        quotation_data: dict,
    ) -> QuotationMaster | None:

        quotation = self.get_by_id(
            quotation_id,
        )

        if quotation is None:
            return None


        for key, value in quotation_data.items():

            setattr(
                quotation,
                key,
                value,
            )


        self.db.commit()

        self.db.refresh(
            quotation
        )

        return quotation


    def delete(
        self,
        quotation_id: int,
    ) -> bool:

        quotation = self.get_by_id(
            quotation_id,
        )

        if quotation is None:
            return False


        self.db.delete(
            quotation,
        )

        self.db.commit()

        return True


    def exists_by_quotation_no(
        self,
        quotation_no: str,
    ) -> bool:

        return (
            self.db.query(QuotationMaster)
            .filter(
                QuotationMaster.quotation_no == quotation_no,
            )
            .first()
            is not None
        )