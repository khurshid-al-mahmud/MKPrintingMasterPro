"""
Product Template Service.

Business Logic Layer
for Product Template Management.
"""

from app.models.product_template import ProductTemplate


class ProductTemplateService:
    """
    Service for Product Template.
    """

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    def create(
        self,
        template_data,
    ) -> ProductTemplate:

        if self.repository.exists_by_template_code(
            template_data.template_code,
        ):
            raise ValueError(
                "Template Code already exists."
            )

        if self.repository.exists_by_template_name(
            template_data.template_name,
        ):
            raise ValueError(
                "Template Name already exists."
            )

        template = ProductTemplate(
            template_code=template_data.template_code,
            template_name=template_data.template_name,
            product_id=template_data.product_id,
            description=template_data.description,
            is_default=template_data.is_default,
        )

        return self.repository.create(template)

    def get_all(
        self,
    ):
        return self.repository.get_all()

    def get_by_id(
        self,
        template_id: int,
    ):
        return self.repository.get_by_id(
            template_id,
        )

    def update(
        self,
        template_id: int,
        template_data,
    ):

        data = template_data.model_dump(
            exclude_unset=True,
        )

        return self.repository.update(
            template_id,
            data,
        )

    def delete(
        self,
        template_id: int,
    ):

        return self.repository.soft_delete(
            template_id,
        )

    def search(
        self,
        keyword: str,
    ):
        print("=" * 50)
        print("SEARCH KEYWORD :", keyword)

        result = self.repository.search(keyword)

        print("TOTAL FOUND :", len(result))
        print("=" * 50)

        return result