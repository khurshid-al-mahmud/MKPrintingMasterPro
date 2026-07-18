"""
Product Repository.

Database access layer
for Product Management.
"""

from sqlalchemy import or_

from app.models.product import Product


class ProductRepository:
    """
    Repository for Product.
    """

    def __init__(
        self,
        db,
    ):
        self.db = db

    def create(
        self,
        product: Product,
    ) -> Product:

        self.db.add(
            product,
        )

        self.db.commit()

        self.db.refresh(
            product,
        )

        return product

    def get_by_id(
        self,
        product_id: int,
    ) -> Product | None:

        return (
            self.db.query(
                Product,
            )
            .filter(
                Product.id == product_id,
                Product.is_active == True,
            )
            .first()
        )

    def get_all(
        self,
    ) -> list[Product]:

        return (
            self.db.query(
                Product,
            )
            .filter(
                Product.is_active == True,
            )
            .all()
        )

    def update(
        self,
        product_id: int,
        product_data: dict,
    ) -> Product | None:

        product = self.get_by_id(
            product_id,
        )

        if product is None:
            return None

        for key, value in product_data.items():
            setattr(
                product,
                key,
                value,
            )

        self.db.commit()

        self.db.refresh(
            product,
        )

        return product

    def soft_delete(
        self,
        product_id: int,
    ) -> bool:

        product = self.get_by_id(
            product_id,
        )

        if product is None:
            return False

        product.is_active = False

        self.db.commit()

        return True

    def search(
        self,
        keyword: str,
    ) -> list[Product]:

        return (
            self.db.query(
                Product,
            )
            .filter(
                Product.is_active == True,
            )
            .filter(
                or_(
                    Product.product_name.ilike(
                        f"%{keyword}%",
                    ),
                    Product.product_code.ilike(
                        f"%{keyword}%",
                    ),
                    Product.product_category.ilike(
                        f"%{keyword}%",
                    ),
                )
            )
            .all()
        )

    def exists_by_product_code(
        self,
        product_code: str,
    ) -> bool:

        return (
            self.db.query(
                Product,
            )
            .filter(
                Product.product_code == product_code,
            )
            .first()
            is not None
        )

    def exists_by_product_name(
        self,
        product_name: str,
    ) -> bool:

        return (
            self.db.query(
                Product,
            )
            .filter(
                Product.product_name == product_name,
            )
            .first()
            is not None
        )