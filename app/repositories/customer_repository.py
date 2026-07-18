"""
Customer Repository.

Database access layer
for Customer Management.
"""

from sqlalchemy import or_

from app.models.customer_profile import CustomerProfile
from app.models.party import Party


class CustomerRepository:
    """
    Repository for Customer Profile.
    """

    def __init__(
        self,
        db,
    ):
        self.db = db


    def create(
        self,
        customer: CustomerProfile,
    ) -> CustomerProfile:

        self.db.add(customer)

        self.db.commit()

        self.db.refresh(customer)

        return customer


    def get_by_id(
        self,
        customer_id: int,
    ) -> CustomerProfile | None:

        return (
            self.db.query(CustomerProfile)
            .filter(
                CustomerProfile.id == customer_id,
                CustomerProfile.is_active == True,
            )
            .first()
        )


    def get_all(
        self,
    ) -> list[CustomerProfile]:

        return (
            self.db.query(CustomerProfile)
            .filter(
                CustomerProfile.is_active == True,
            )
            .all()
        )


    def update(
        self,
        customer_id: int,
        customer_data: dict,
    ) -> CustomerProfile | None:

        customer = self.get_by_id(customer_id)

        if customer is None:
            return None


        for key, value in customer_data.items():
            setattr(
                customer,
                key,
                value,
            )


        self.db.commit()

        self.db.refresh(customer)

        return customer


    def soft_delete(
        self,
        customer_id: int,
    ) -> bool:

        customer = self.get_by_id(customer_id)

        if customer is None:
            return False


        customer.is_active = False

        self.db.commit()

        return True


    def search(
        self,
        keyword: str,
    ) -> list[CustomerProfile]:

        return (
            self.db.query(CustomerProfile)
            .join(
                Party,
                CustomerProfile.party_id == Party.id,
            )
            .filter(
                CustomerProfile.is_active == True,
            )
            .filter(
                or_(
                    Party.party_name.ilike(
                        f"%{keyword}%"
                    ),
                    Party.mobile.ilike(
                        f"%{keyword}%"
                    ),
                )
            )
            .all()
        )