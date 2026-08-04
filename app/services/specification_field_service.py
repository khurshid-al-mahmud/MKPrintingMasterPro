"""
Specification Field Service.

Business Logic Layer
for Specification Field Management.
"""

from app.models.specification_field import SpecificationField


class SpecificationFieldService:
    """
    Service for Specification Field.
    """

    def __init__(
        self,
        repository,
    ):
        self.repository = repository

    # ==========================
    # CREATE
    # ==========================

    def create(
        self,
        field_data,
    ) -> SpecificationField:

        existing = self.repository.get_by_code(
            field_data.field_code,
        )

        if existing:
            raise ValueError(
                "Specification Field Code already exists."
            )

        field = SpecificationField(
            field_code=field_data.field_code,
            field_name_en=field_data.field_name_en,
            field_name_bn=field_data.field_name_bn,
            description=field_data.description,
            group_id=field_data.group_id,

            data_type=field_data.data_type,
            input_control=field_data.input_control,

            placeholder_en=field_data.placeholder_en,
            placeholder_bn=field_data.placeholder_bn,
            default_value=field_data.default_value,
            help_text=field_data.help_text,
            icon=field_data.icon,

            is_required=field_data.is_required,
            is_editable=field_data.is_editable,
            is_visible=field_data.is_visible,
            is_calculated=field_data.is_calculated,
            is_system_field=field_data.is_system_field,

            display_order=field_data.display_order,
            width=field_data.width,

            minimum_value=field_data.minimum_value,
            maximum_value=field_data.maximum_value,
            minimum_length=field_data.minimum_length,
            maximum_length=field_data.maximum_length,
            regex_pattern=field_data.regex_pattern,
            validation_message=field_data.validation_message,

            unit=field_data.unit,
            formula_reference=field_data.formula_reference,

            is_active=field_data.is_active,

            # Authentication যুক্ত হলে এখানে current_user.username ব্যবহার করবে
            created_by="system",
            updated_by="system",
        )

        return self.repository.create(field)

    # ==========================
    # GET ALL
    # ==========================

    def get_all(self):

        return self.repository.get_all()

    # ==========================
    # GET BY ID
    # ==========================

    def get_by_id(
        self,
        field_id: int,
    ):

        return self.repository.get_by_id(
            field_id,
        )

    # ==========================
    # GET BY GROUP
    # ==========================

    def get_by_group(
        self,
        group_id: int,
    ):

        return self.repository.get_by_group(
            group_id,
        )

    # ==========================
    # GET BY CODE
    # ==========================

    def get_by_code(
        self,
        field_code: str,
    ):

        return self.repository.get_by_code(
            field_code,
        )

    # ==========================
    # REQUIRED FIELDS
    # ==========================

    def get_required_fields(
        self,
        group_id: int,
    ):

        return self.repository.get_required_fields(
            group_id,
        )

    # ==========================
    # CALCULATED FIELDS
    # ==========================

    def get_calculated_fields(
        self,
        group_id: int,
    ):

        return self.repository.get_calculated_fields(
            group_id,
        )

    # ==========================
    # UPDATE
    # ==========================

    def update(
        self,
        field_id: int,
        field_data,
    ):

        field = self.repository.get_by_id(
            field_id,
        )

        if field is None:
            return None

        data = field_data.model_dump(
            exclude_unset=True,
        )

        # Authentication যুক্ত হলে current_user.username ব্যবহার করবে
        data["updated_by"] = "system"

        for key, value in data.items():
            setattr(
                field,
                key,
                value,
            )

        return self.repository.update(
            field,
        )

    # ==========================
    # DELETE (Soft Delete)
    # ==========================

    def delete(
        self,
        field_id: int,
    ):

        field = self.repository.get_by_id(
            field_id,
        )

        if field is None:
            return False

        field.is_active = False
        field.updated_by = "system"

        self.repository.update(
            field,
        )

        return True