"""
MKPrintingMasterPro ERP
Build-015B

Validation Engine

Purpose:
Dynamic Validation Engine
for Specification Fields.

Status:
Production Ready
"""

import re


class ValidationEngine:

    def validate_required(
        self,
        value,
        field,
    ):

        if field.is_required:

            if value is None:

                return False

            if str(value).strip() == "":

                return False

        return True

    # -------------------------------------

    def validate_minimum(
        self,
        value,
        field,
    ):

        if field.minimum_value is None:

            return True

        try:

            return float(value) >= float(
                field.minimum_value
            )

        except Exception:

            return True

    # -------------------------------------

    def validate_maximum(
        self,
        value,
        field,
    ):

        if field.maximum_value is None:

            return True

        try:

            return float(value) <= float(
                field.maximum_value
            )

        except Exception:

            return True

    # -------------------------------------

    def validate_min_length(
        self,
        value,
        field,
    ):

        if field.minimum_length is None:

            return True

        return len(str(value)) >= field.minimum_length

    # -------------------------------------

    def validate_max_length(
        self,
        value,
        field,
    ):

        if field.maximum_length is None:

            return True

        return len(str(value)) <= field.maximum_length

    # -------------------------------------

    def validate_regex(
        self,
        value,
        field,
    ):

        if not field.regex_pattern:

            return True

        return re.fullmatch(
            field.regex_pattern,
            str(value),
        ) is not None

    # -------------------------------------

    def validate(
        self,
        value,
        field,
    ):

        if not self.validate_required(
            value,
            field,
        ):

            return (
                False,
                "Required Field"
            )

        if not self.validate_minimum(
            value,
            field,
        ):

            return (
                False,
                "Minimum Value Error"
            )

        if not self.validate_maximum(
            value,
            field,
        ):

            return (
                False,
                "Maximum Value Error"
            )

        if not self.validate_min_length(
            value,
            field,
        ):

            return (
                False,
                "Minimum Length Error"
            )

        if not self.validate_max_length(
            value,
            field,
        ):

            return (
                False,
                "Maximum Length Error"
            )

        if not self.validate_regex(
            value,
            field,
        ):

            return (
                False,
                "Invalid Format"
            )

        return (
            True,
            "OK"
        )