"""
Golden Date-Time Service.

Central Date-Time Engine
for MKPrintingMasterPro ERP.

Supports:
- AUTO / MANUAL date
- DATE_ONLY
- TIME_ONLY
- DATE_TIME
- Multiple display formats
- System timezone
"""

from datetime import datetime, date
from zoneinfo import ZoneInfo

from app.core.date_time import get_current_datetime


# -----------------------------------
# Supported Formats
# -----------------------------------

DATE_FORMATS = {

    "DD-MM-YYYY": "%d-%m-%Y",

    "YYYY-MM-DD": "%Y-%m-%d",

    "MM-DD-YYYY": "%m-%d-%Y",

    "DD/MM/YYYY": "%d/%m/%Y",

    "YYYY/MM/DD": "%Y/%m/%d",

    "MM/DD/YYYY": "%m/%d/%Y",

}


TIME_FORMATS = {

    "24H": "%H:%M:%S",

    "24H_SHORT": "%H:%M",

    "12H": "%I:%M:%S %p",

    "12H_SHORT": "%I:%M %p",

}


# -----------------------------------
# Timezone
# -----------------------------------

def get_timezone(
    timezone_name: str = "Asia/Dhaka",
):
    """
    Return timezone object.
    """

    return ZoneInfo(timezone_name)



# -----------------------------------
# Date Only
# -----------------------------------

def get_date(
    format_name: str = "YYYY-MM-DD",
):
    """
    Return formatted date only.
    """

    now = get_current_datetime()

    fmt = DATE_FORMATS.get(
        format_name,
        "%Y-%m-%d",
    )

    return now.strftime(fmt)



# -----------------------------------
# Time Only
# -----------------------------------

def get_time(
    format_name: str = "24H",
):
    """
    Return formatted time only.
    """

    now = get_current_datetime()

    fmt = TIME_FORMATS.get(
        format_name,
        "%H:%M:%S",
    )

    return now.strftime(fmt)



# -----------------------------------
# Date + Time
# -----------------------------------

def get_datetime(
    date_format: str = "YYYY-MM-DD",
    time_format: str = "24H",
):
    """
    Return formatted date time.
    """

    now = get_current_datetime()


    date_part = now.strftime(
        DATE_FORMATS.get(
            date_format,
            "%Y-%m-%d",
        )
    )


    time_part = now.strftime(
        TIME_FORMATS.get(
            time_format,
            "%H:%M:%S",
        )
    )


    return f"{date_part} {time_part}"



# -----------------------------------
# Manual / Auto Date
# -----------------------------------

def resolve_document_date(
    mode: str = "AUTO",
    manual_date: date | None = None,
):
    """
    Resolve document date.

    AUTO:
        Current date

    MANUAL:
        User provided date
    """

    if mode.upper() == "MANUAL":

        if manual_date:
            return manual_date

    return get_current_datetime().date()