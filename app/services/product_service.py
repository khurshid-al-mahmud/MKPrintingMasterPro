"""
Product Service.

Business Logic Layer
for Product Management.
"""

from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
)


class ProductService:
    """
    Service layer for Product Management.
    """

    def __init__(
        self,
        repository: ProductRepository,
    ) -> None:
        self.repository = repository


    def create(
        self,
        product: ProductCreate,
    ) -> Product:
        """
        Create a new product.
        """

        if self.repository.exists_by_product_code(
            product.product_code,
        ):
            raise ValueError(
                "Product code already exists.",
            )


        if self.repository.exists_by_product_name(
            product.product_name,
        ):
            raise ValueError(
                "Product name already exists.",
            )


        new_product = Product(
            product_code=product.product_code,
            product_name=product.product_name,
            category_id=product.category_id,
            printing_type=product.printing_type,
            unit=product.unit,
        )


        return self.repository.create(
            new_product,
        )


    def get_all(
        self,
    ) -> list[Product]:
        """
        Get all active products.
        """

        return self.repository.get_all()


    def get_by_id(
        self,
        product_id: int,
    ) -> Product | None:
        """
        Get product by ID.
        """

        return self.repository.get_by_id(
            product_id,
        )


    def update(
        self,
        product_id: int,
        product_data: ProductUpdate,
    ) -> Product | None:
        """
        Update product.
        """

        return self.repository.update(
            product_id,
            product_data.model_dump(
                exclude_unset=True,
            ),
        )


    def delete(
        self,
        product_id: int,
    ) -> bool:
        """
        Soft delete product.
        """

        return self.repository.soft_delete(
            product_id,
        )


    def search(
        self,
        keyword: str,
    ) -> list[Product]:
        """
        Search products.
        """

        return self.repository.search(
            keyword,
        )