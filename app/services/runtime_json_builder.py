"""
MKPrintingMasterPro ERP
Build-016B

Runtime JSON Builder

Purpose:
Build Final Runtime JSON
for ERP / API / AI Assistant

Status:
Build-016 Freeze
"""

from typing import Any


class RuntimeJSONBuilder:

    # --------------------------------------------------
    # Build Complete Runtime JSON
    # --------------------------------------------------

    def build(
        self,
        runtime_data: dict,
    ) -> dict:

        return {

            "success": runtime_data.get(
                "success",
                True,
            ),

            "template": self.build_template(

                runtime_data["template"]

            ),

            "groups": [

                self.build_group(group)

                for group in runtime_data["groups"]

            ],

            "validation":

                runtime_data.get(

                    "validation",

                    {}

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

            "cost":

                runtime_data.get(

                    "cost",

                    {}

                ),

            "pricing":

                runtime_data.get(

                    "pricing",

                    {}

                ),

            "quotation":

                runtime_data.get(

                    "quotation",

                    {}

                ),

        }

    # --------------------------------------------------
    # Template
    # --------------------------------------------------

    def build_template(
        self,
        template,
    ) -> dict:

        return {

            "id": getattr(
                template,
                "id",
                None,
            ),

            "template_code": getattr(
                template,
                "template_code",
                None,
            ),

            "template_name_en": getattr(
                template,
                "template_name_en",
                None,
            ),

            "template_name_bn": getattr(
                template,
                "template_name_bn",
                None,
            ),

            "version": getattr(
                template,
                "current_version",
                None,
            ),

        }

    # --------------------------------------------------
    # Group
    # --------------------------------------------------

    def build_group(
        self,
        group_data,
    ):

        group = group_data["group"]

        return {

            "id": getattr(group, "id", None),

            "group_code": getattr(
                group,
                "group_code",
                None,
            ),

            "group_name_en": getattr(
                group,
                "group_name_en",
                None,
            ),

            "group_name_bn": getattr(
                group,
                "group_name_bn",
                None,
            ),

            "display_order": getattr(
                group,
                "display_order",
                None,
            ),

            "fields": [

                self.build_field(field)

                for field in group_data.get(
                    "fields",
                    [],
                )

            ],

        }

    # --------------------------------------------------
    # Field
    # --------------------------------------------------

    def build_field(
        self,
        field_data,
    ):

        field = field_data["field"]

        return {

            "id": getattr(field, "id", None),

            "field_code": getattr(
                field,
                "field_code",
                None,
            ),

            "field_name_en": getattr(
                field,
                "field_name_en",
                None,
            ),

            "field_name_bn": getattr(
                field,
                "field_name_bn",
                None,
            ),

            "field_type": getattr(
                field,
                "field_type",
                None,
            ),

            "required": getattr(
                field,
                "is_required",
                False,
            ),

            "readonly": getattr(
                field,
                "is_readonly",
                False,
            ),

            "display_order": getattr(
                field,
                "display_order",
                0,
            ),

            "default_value": getattr(
                field,
                "default_value",
                None,
            ),

            "options": [

                self.build_option(option)

                for option in field_data.get(
                    "options",
                    [],
                )

            ],

        }

    # --------------------------------------------------
    # Option
    # --------------------------------------------------

    def build_option(
        self,
        option,
    ):

        return {

            "id": getattr(option, "id", None),

            "option_code": getattr(
                option,
                "option_code",
                None,
            ),

            "option_label": getattr(
                option,
                "option_label",
                None,
            ),

            "option_value": getattr(
                option,
                "option_value",
                None,
            ),

            "display_order": getattr(
                option,
                "display_order",
                0,
            ),

        }

    # --------------------------------------------------

    def export(
        self,
        runtime_data,
    ):

        return self.build(
            runtime_data
        )