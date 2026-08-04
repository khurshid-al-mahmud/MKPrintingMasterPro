"""
Field Option Service.

Business Logic Layer
for Field Option Management.
"""

from app.models.field_option import FieldOption


class FieldOptionService:
    """
    Service for Field Option.
    """

    def __init__(self, repository):
        self.repository = repository

    # ==========================
    # CREATE
    # ==========================

    def create(self, option_data) -> FieldOption:

        existing = self.repository.get_by_code(
            option_data.option_code
        )

        if existing:
            raise ValueError(
                "Field Option Code already exists."
            )

        option = FieldOption(
            field_id=option_data.field_id,

            option_code=option_data.option_code,

            option_name_en=option_data.option_name_en,
            option_name_bn=option_data.option_name_bn,

            description=option_data.description,

            option_value=option_data.option_value,

            display_order=option_data.display_order,

            is_default=option_data.is_default,

            is_active=option_data.is_active,

            created_by="system",
            updated_by="system",
        )

        return self.repository.create(option)

    # ==========================
    # GET ALL
    # ==========================

    def get_all(self):

        return self.repository.get_all()

    # ==========================
    # GET BY ID
    # ==========================

    def get_by_id(self, option_id: int):

        return self.repository.get_by_id(
            option_id
        )

    # ==========================
    # GET BY FIELD
    # ==========================

    def get_by_field(self, field_id: int):

        return self.repository.get_by_field(
            field_id
        )

    # ==========================
    # GET BY CODE
    # ==========================

    def get_by_code(
        self,
        option_code: str,
    ):

        return self.repository.get_by_code(
            option_code
        )

    # ==========================
    # UPDATE
    # ==========================

    def update(
        self,
        option_id: int,
        option_data,
    ):

        option = self.repository.get_by_id(
            option_id
        )

        if option is None:
            return None

        data = option_data.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(option, key, value)

        option.updated_by = "system"

        return self.repository.update(
            option
        )

    # ==========================
    # DELETE
    # ==========================

    def delete(
        self,
        option_id: int,
    ):

        option = self.repository.get_by_id(
            option_id
        )

        if option is None:
            return False

        option.is_active = False

        option.updated_by = "system"

        self.repository.update(option)

        return True