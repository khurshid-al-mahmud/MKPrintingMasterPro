from sqlalchemy import or_

from app.models.product_category import ProductCategory


class ProductCategoryRepository:

    def __init__(self, db):
        self.db = db

    def create(self, category):
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def get_all(self):
        return (
            self.db.query(ProductCategory)
            .filter(ProductCategory.is_active == True)
            .order_by(ProductCategory.sort_order)
            .all()
        )

    def get_by_id(self, category_id):
        return (
            self.db.query(ProductCategory)
            .filter(ProductCategory.id == category_id)
            .first()
        )

    def exists_by_code(self, code):
        return (
            self.db.query(ProductCategory)
            .filter(ProductCategory.category_code == code)
            .first()
            is not None
        )

    def exists_by_name(self, name):
        return (
            self.db.query(ProductCategory)
            .filter(ProductCategory.category_name == name)
            .first()
            is not None
        )

    def update(self, category, data):
        for key, value in data.items():
            setattr(category, key, value)

        self.db.commit()
        self.db.refresh(category)
        return category

    def soft_delete(self, category):
        category.is_active = False
        self.db.commit()

    def search(self, keyword):
        return (
            self.db.query(ProductCategory)
            .filter(
                or_(
                    ProductCategory.category_name.ilike(f"%{keyword}%"),
                    ProductCategory.category_code.ilike(f"%{keyword}%"),
                )
            )
            .all()
        )