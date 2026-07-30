from app.models.product_category import ProductCategory
from app.repositories.product_category_repository import (
    ProductCategoryRepository,
)
from app.schemas.product_category import (
    ProductCategoryCreate,
    ProductCategoryUpdate,
)


class ProductCategoryService:

    def __init__(self, repository: ProductCategoryRepository):
        self.repository = repository

    def create(self, data: ProductCategoryCreate):

        if self.repository.exists_by_code(data.category_code):
            raise ValueError("Category Code already exists.")

        if self.repository.exists_by_name(data.category_name):
            raise ValueError("Category Name already exists.")

        category = ProductCategory(
            category_code=data.category_code,
            category_name=data.category_name,
            description=data.description,
            sort_order=data.sort_order,
        )

        return self.repository.create(category)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, category_id):
        return self.repository.get_by_id(category_id)

    def update(self, category_id, data: ProductCategoryUpdate):
        category = self.repository.get_by_id(category_id)

        if category is None:
            return None

        return self.repository.update(
            category,
            data.model_dump(exclude_unset=True),
        )

    def delete(self, category_id):
        category = self.repository.get_by_id(category_id)

        if category is None:
            return False

        self.repository.soft_delete(category)

        return True

    def search(self, keyword):
        return self.repository.search(keyword)