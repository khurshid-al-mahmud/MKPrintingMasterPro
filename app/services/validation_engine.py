"""
MKPrintingMasterPro ERP
Build-016A

Validation Engine

Purpose:
Enterprise Runtime Validation Engine

Status:
Production Ready
"""

import re
from typing import Dict, List


class ValidationEngine:

    # --------------------------------------------------

    def validate_required(self, value, field):

        if getattr(field, "is_required", False):

            if value is None:
                return False

            if str(value).strip() == "":
                return False

        return True

    # --------------------------------------------------

    def validate_minimum(self, value, field):

        minimum = getattr(field, "minimum_value", None)

        if minimum is None:
            return True

        try:
            return float(value) >= float(minimum)
        except Exception:
            return True

    # --------------------------------------------------

    def validate_maximum(self, value, field):

        maximum = getattr(field, "maximum_value", None)

        if maximum is None:
            return True

        try:
            return float(value) <= float(maximum)
        except Exception:
            return True

    # --------------------------------------------------

    def validate_min_length(self, value, field):

        minimum = getattr(field, "minimum_length", None)

        if minimum is None:
            return True

        return len(str(value)) >= minimum

    # --------------------------------------------------

    def validate_max_length(self, value, field):

        maximum = getattr(field, "maximum_length", None)

        if maximum is None:
            return True

        return len(str(value)) <= maximum

    # --------------------------------------------------

    def validate_regex(self, value, field):

        pattern = getattr(field, "regex_pattern", None)

        if not pattern:
            return True

        return re.fullmatch(pattern, str(value)) is not None

    # --------------------------------------------------

    def validate_field(self, value, field):

        if not self.validate_required(value, field):
            return False, "Required Field"

        if not self.validate_minimum(value, field):
            return False, "Minimum Value Error"

        if not self.validate_maximum(value, field):
            return False, "Maximum Value Error"

        if not self.validate_min_length(value, field):
            return False, "Minimum Length Error"

        if not self.validate_max_length(value, field):
            return False, "Maximum Length Error"

        if not self.validate_regex(value, field):
            return False, "Invalid Format"

        return True, "OK"

    # --------------------------------------------------
    # Enterprise Runtime Validation
    # --------------------------------------------------

    def validate(self, values: Dict, template: Dict):

        errors: List[Dict] = []

        groups = template.get("groups", [])

        for group in groups:

            for field_info in group["fields"]:

                field = field_info["field"]

                field_name = field.field_name

                value = values.get(field_name)

                status, message = self.validate_field(
                    value,
                    field,
                )

                if not status:

                    errors.append({

                        "field": field_name,

                        "message": message,

                    })

        return {

            "valid": len(errors) == 0,

            "errors": errors,

        }