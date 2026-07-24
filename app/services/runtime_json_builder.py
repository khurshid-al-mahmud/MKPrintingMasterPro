"""
MKPrintingMasterPro ERP
Build-015B

Runtime JSON Builder

Purpose:
Converts Dynamic Runtime Objects into
Frontend / API / AI Ready JSON.

Status:
Production Ready
"""

from typing import Any


class RuntimeJSONBuilder:

    # --------------------------------------------------
    # Build Complete Runtime JSON
    # --------------------------------------------------

    def build(self, runtime_data: dict) -> dict:

        return {

            "template": self.build_template(

                runtime_data["template"]

            ),

            "groups": [

                self.build_group(group)

                for group in runtime_data["groups"]

            ],

            "validation_errors":

                runtime_data.get(

                    "validation_errors",

                    []

                ),

            "dependency":

                runtime_data.get(

                    "dependency",

                    {}

                ),

            "formula":

                runtime_data.get(

                    "formula",

                    {}

                ),

        }

    # --------------------------------------------------
    # Template
    # --------------------------------------------------

    def build_template(self, template) -> dict:

        return {

            "id": template.id,

            "template_code": template.template_code,

            "template_name_en": template.template_name_en,

            "template_name_bn": template.template_name_bn,

            "version":

                getattr(

                    template,

                    "current_version",

                    None,

                ),

        }

    # --------------------------------------------------
    # Group
    # --------------------------------------------------

    def build_group(self, group_data: dict) -> dict:

        group = group_data["group"]

        return {

            "id": group.id,

            "group_code": group.group_code,

            "group_name_en": group.group_name_en,

            "group_name_bn": group.group_name_bn,

            "display_order":

                group.display_order,

            "fields": [

                self.build_field(field)

                for field in group_data["fields"]

            ],

        }

    # --------------------------------------------------
    # Field
    # --------------------------------------------------

    def build_field(self, field_data: dict) -> dict:

        field = field_data["field"]

        options = field_data["options"]

        return {

            "id": field.id,

            "field_code": field.field_code,

            "field_name_en":

                field.field_name_en,

            "field_name_bn":

                field.field_name_bn,

            "field_type":

                field.field_type,

            "required":

                field.is_required,

            "readonly":

                field.is_readonly,

            "display_order":

                field.display_order,

            "default_value":

                field.default_value,

            "options": [

                self.build_option(option)

                for option in options

            ],

        }

    # --------------------------------------------------
    # Option
    # --------------------------------------------------

    def build_option(self, option) -> dict:

        return {

            "id": option.id,

            "option_code":

                option.option_code,

            "option_label":

                option.option_label,

            "option_value":

                option.option_value,

            "display_order":

                option.display_order,

        }

    # --------------------------------------------------
    # Generic Export
    # --------------------------------------------------

    def export(

        self,

        runtime_data: dict,

    ) -> dict:

        return self.build(

            runtime_data

        )