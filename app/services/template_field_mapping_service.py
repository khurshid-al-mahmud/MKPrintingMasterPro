"""
MKPrintingMasterPro ERP
Build-016

Template Field Mapping Service

Purpose:
Business Logic Layer for
Template Field Mapping Management.

Status:
Production Ready
"""

from app.models.template_field_mapping import (
    TemplateFieldMapping,
)


class TemplateFieldMappingService:
    """
    Service for Template Field Mapping.
    """

    def __init__(
        self,
        repository,
    ):
        self.repository = repository


    # =====================================
    # CREATE
    # =====================================

    def create(
        self,
        mapping_data,
    ) -> TemplateFieldMapping:


        mapping = TemplateFieldMapping(

            template_id=mapping_data.template_id,

            field_id=mapping_data.field_id,

            is_required=mapping_data.is_required,

            is_visible=mapping_data.is_visible,

            is_editable=mapping_data.is_editable,

            default_value=mapping_data.default_value,

            display_order=mapping_data.display_order,

            group_order=mapping_data.group_order,

            column_width=mapping_data.column_width,

            show_in_quotation=mapping_data.show_in_quotation,

            show_in_job_order=mapping_data.show_in_job_order,

            show_in_production=mapping_data.show_in_production,

            show_in_invoice=mapping_data.show_in_invoice,

            validation_override=mapping_data.validation_override,

            formula_override=mapping_data.formula_override,

            is_active=mapping_data.is_active,

            created_by="system",

            updated_by="system",
        )


        return self.repository.create_mapping(
            mapping
        )



    # =====================================
    # GET ALL
    # =====================================

    def get_all(self):

        return (
            self.repository
            .get_all_active()
        )



    # =====================================
    # GET BY ID
    # =====================================

    def get_by_id(
        self,
        mapping_id: int,
    ):

        return (
            self.repository
            .get_by_id(mapping_id)
        )



    # =====================================
    # GET BY TEMPLATE
    # =====================================

    def get_by_template(
        self,
        template_id: int,
    ):

        return (
            self.repository
            .get_by_template(
                template_id
            )
        )



    # =====================================
    # UPDATE
    # =====================================

    def update(
        self,
        mapping_id: int,
        mapping_data,
    ):


        mapping = (
            self.repository
            .get_by_id(mapping_id)
        )


        if mapping is None:
            return None



        data = mapping_data.model_dump(
            exclude_unset=True
        )



        for key, value in data.items():

            setattr(
                mapping,
                key,
                value
            )


        mapping.updated_by = "system"


        self.repository.update_mapping()


        return mapping



    # =====================================
    # DELETE SOFT
    # =====================================

    def delete(
        self,
        mapping_id: int,
    ):


        mapping = (
            self.repository
            .get_by_id(mapping_id)
        )


        if mapping is None:
            return False



        self.repository.delete_mapping(
            mapping
        )


        return True