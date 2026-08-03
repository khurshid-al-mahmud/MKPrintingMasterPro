"""
Product Template Repository.

Database access layer
for Product Template Management.
"""

from sqlalchemy import or_

from app.models.product_template import ProductTemplate


class ProductTemplateRepository:
    """
    Repository for Product Template.
    """

    def __init__(
        self,
        db,
    ):
        self.db = db


    def create(
        self,
        template: ProductTemplate,
    ) -> ProductTemplate:

        self.db.add(template)

        self.db.commit()

        self.db.refresh(template)

        return template


    def get_by_id(
        self,
        template_id: int,
    ) -> ProductTemplate | None:

        return (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.id == template_id,
                ProductTemplate.is_active == True,
            )
            .first()
        )


    def get_all(
        self,
    ) -> list[ProductTemplate]:

        return (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.is_active == True,
            )
            .all()
        )


    def update(
        self,
        template_id: int,
        template_data: dict,
    ) -> ProductTemplate | None:

        template = self.get_by_id(template_id)

        if template is None:
            return None

        for key, value in template_data.items():
            setattr(
                template,
                key,
                value,
            )

        self.db.commit()

        self.db.refresh(template)

        return template


    def soft_delete(
        self,
        template_id: int,
    ) -> bool:

        template = self.get_by_id(template_id)

        if template is None:
            return False

        template.is_active = False

        self.db.commit()

        return True


    def search(
        self,
        keyword: str,
    ) -> list[ProductTemplate]:

        return (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.is_active == True,
            )
            .filter(
                or_(
                    ProductTemplate.template_name.ilike(
                        f"%{keyword}%"
                    ),
                    ProductTemplate.template_code.ilike(
                        f"%{keyword}%"
                    ),
                )
            )
            .all()
        )


    def exists_by_template_code(
        self,
        template_code: str,
    ) -> bool:

        return (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.template_code == template_code,
            )
            .first()
            is not None
        )


    def exists_by_template_name(
        self,
        template_name: str,
    ) -> bool:

        return (
            self.db.query(ProductTemplate)
            .filter(
                ProductTemplate.template_name == template_name,
            )
            .first()
            is not None
        )