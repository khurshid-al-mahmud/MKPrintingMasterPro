"""
Customer Service.

Business Logic Layer
for Customer Management.
"""

from app.models.customer_profile import CustomerProfile
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
)


class CustomerService:
    """
    Service layer for Customer management.
    """

    def __init__(
        self,
        repository: CustomerRepository,
    ) -> None:
        self.repository = repository

    def create(
        self,
        customer: CustomerCreate,
    ) -> CustomerProfile:
        """
        Create customer.
        """

        new_customer = CustomerProfile(
            party_id=customer.party_id,
            customer_number=customer.customer_number,
            customer_category=customer.customer_category,
            credit_limit=customer.credit_limit,
            credit_days=customer.credit_days,
            price_category=customer.price_category,
            discount_rate=customer.discount_rate,
        )

        return self.repository.create(
            new_customer,
        )

    def get_by_id(
        self,
        customer_id: int,
    ) -> CustomerProfile | None:
        """
        Get customer by ID.
        """

        return self.repository.get_by_id(
            customer_id,
        )

    def get_all(
        self,
    ) -> list[CustomerProfile]:
        """
        Get all customers.
        """

        return self.repository.get_all()

    def update(
        self,
        customer_id: int,
        customer_data: CustomerUpdate,
    ) -> CustomerProfile | None:
        """
        Update customer.
        """

        return self.repository.update(
            customer_id,
            customer_data.model_dump(
                exclude_unset=True,
            ),
        )

    def delete(
        self,
        customer_id: int,
    ) -> bool:
        """
        Soft delete customer.
        """

        return self.repository.soft_delete(
            customer_id,
        )

    def search(
        self,
        keyword: str,
    ) -> list[CustomerProfile]:
        """
        Search customers.
        """

        return self.repository.search(
            keyword,
        )