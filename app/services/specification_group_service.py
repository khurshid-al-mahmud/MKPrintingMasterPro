"""
Specification Group Service.

Business Logic Layer
for Specification Group Management.
"""

from app.models.specification_group import SpecificationGroup


class SpecificationGroupService:
    """
    Service for Specification Group.
    """

    def __init__(
        self,
        repository,
    ):
        self.repository = repository


    def create(
        self,
        group_data,
    ) -> SpecificationGroup:

        existing = self.repository.get_by_code(
            group_data.group_code,
        )

        if existing:
            raise ValueError(
                "Specification Group Code already exists."
            )

        group = SpecificationGroup(
            group_code=group_data.group_code,
            group_name=group_data.group_name,
            template_id=group_data.template_id,
            display_order=group_data.display_order,
            description=group_data.description,
            is_active=group_data.is_active,
        )

        return self.repository.create(group)


    def get_all(
        self,
    ):
        return self.repository.get_active_groups()


    def get_by_id(
        self,
        group_id: int,
    ):
        return self.repository.get_by_id(
            group_id,
        )


    def get_by_template(
        self,
        template_id: int,
    ):
        return self.repository.get_by_template(
            template_id,
        )


    def get_by_code(
        self,
        group_code: str,
    ):
        return self.repository.get_by_code(
            group_code,
        )


    def update(
        self,
        group_id: int,
        group_data,
    ):

        group = self.repository.get_by_id(
            group_id,
        )

        if group is None:
            return None

        data = group_data.model_dump(
            exclude_unset=True,
        )

        for key, value in data.items():
            setattr(
                group,
                key,
                value,
            )

        return self.repository.update(
            group,
        )


    def delete(
        self,
        group_id: int,
    ):

        group = self.repository.get_by_id(
            group_id,
        )

        if group is None:
            return False

        group.is_active = False

        self.repository.update(
            group,
        )

        return True