"""
MKPrintingMasterPro ERP

Specification Runtime Service

Phase-8
Dynamic Runtime Engine
"""

from sqlalchemy.orm import Session

from app.repositories.template_field_mapping_repository import (
    TemplateFieldMappingRepository,
)

from app.repositories.specification_field_repository import (
    SpecificationFieldRepository,
)

from app.repositories.field_option_repository import (
    FieldOptionRepository,
)


class SpecificationRuntimeService:
    """
    Dynamic Runtime Resolver
    """

    def __init__(
        self,
        db: Session,
    ):
        self.db = db

        self.template_mapping_repo = (
            TemplateFieldMappingRepository(db)
        )

        self.field_repo = (
            SpecificationFieldRepository(db)
        )

        self.option_repo = (
            FieldOptionRepository(db)
        )

    # ==========================================
    # Runtime Template
    # ==========================================

    def get_template_runtime(
        self,
        template_id: int,
    ):

        mappings = (
            self.template_mapping_repo.get_by_template(
                template_id
            )
        )

        fields = []

        for mapping in mappings:

            field = self.field_repo.get_by_id(
                mapping.field_id
            )

            if field is None:
                continue

            options = self.option_repo.get_by_field(
                field.id
            )

            option_list = []

            for option in options:

                option_list.append(
                    {
                        "id": option.id,
                        "option_code": option.option_code,
                        "option_name_en": option.option_name_en,
                        "option_name_bn": option.option_name_bn,
                        "option_value": option.option_value,
                        "is_default": option.is_default,
                        "display_order": option.display_order,
                    }
                )

            fields.append(
                {
                    # -----------------------------
                    # Field Information
                    # -----------------------------
                    "field_id": field.id,
                    "field_name_en": field.field_name_en,
                    "field_name_bn": field.field_name_bn,
                    "field_type": field.data_type,
                    "input_control": field.input_control,

                    # -----------------------------
                    # Runtime Metadata
                    # -----------------------------
                    "group_id": field.group_id,
                    "placeholder_en": field.placeholder_en,
                    "placeholder_bn": field.placeholder_bn,
                    "help_text": field.help_text,
                    "icon": field.icon,

                    # -----------------------------
                    # Field Behaviour
                    # -----------------------------
                    "is_calculated": field.is_calculated,
                    "is_system_field": field.is_system_field,
                    "is_required_field": field.is_required,
                    "is_visible_field": field.is_visible,
                    "is_editable_field": field.is_editable,

                    # -----------------------------
                    # Mapping Behaviour
                    # -----------------------------
                    "required": mapping.is_required,
                    "visible": mapping.is_visible,
                    "editable": mapping.is_editable,
                    "default_value": mapping.default_value,
                    "display_order": mapping.display_order,

                    # -----------------------------
                    # Dropdown Options
                    # -----------------------------
                    "options": option_list,
                }
            )

        return {
            "template_id": template_id,
            "fields": fields,
        }