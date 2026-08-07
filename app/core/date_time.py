"""
Golden Date-Time System

Central Date and Time Management
for MKPrintingMasterPro ERP.
"""

from datetime import date, datetime
from zoneinfo import ZoneInfo


DEFAULT_TIMEZONE = "Asia/Dhaka"


def get_current_date(
    timezone: str = DEFAULT_TIMEZONE,
) -> date:
    """
    Return current date based on timezone.
    """

    now = datetime.now(
        ZoneInfo(timezone)
    )

    return now.date()



def get_current_datetime(
    timezone: str = DEFAULT_TIMEZONE,
) -> datetime:
    """
    Return current datetime based on timezone.
    """

    return datetime.now(
        ZoneInfo(timezone)
    )



def format_date(
    value: date | datetime,
    format_code: str = "YYYY-MM-DD",
) -> str:
    """
    Format date according to ERP setting.
    """

    if isinstance(value, datetime):
        value = value.date()


    formats = {

        "YYYY-MM-DD": "%Y-%m-%d",

        "YYYY/MM/DD": "%Y/%m/%d",

        "DD-MM-YYYY": "%d-%m-%Y",

        "DD/MM/YYYY": "%d/%m/%Y",

        "MM-DD-YYYY": "%m-%d-%Y",

        "MM/DD/YYYY": "%m/%d/%Y",

        "DD MMM YYYY": "%d %b %Y",

        "DD MMMM YYYY": "%d %B %Y",

        "MMM DD, YYYY": "%b %d, %Y",

        "MMMM DD, YYYY": "%B %d, %Y",

    }


    selected_format = formats.get(
        format_code,
        "%Y-%m-%d",
    )


    return value.strftime(
        selected_format
    )



def format_datetime(
    value: datetime,
    format_code: str = "YYYY-MM-DD HH:mm:ss",
) -> str:
    """
    Format datetime according to ERP setting.
    """

    formats = {

        "YYYY-MM-DD HH:mm":
            "%Y-%m-%d %H:%M",

        "YYYY-MM-DD HH:mm:ss":
            "%Y-%m-%d %H:%M:%S",

        "DD-MM-YYYY HH:mm":
            "%d-%m-%Y %H:%M",

        "DD-MM-YYYY HH:mm:ss":
            "%d-%m-%Y %H:%M:%S",

        "DD-MM-YYYY hh:mm AM":
            "%d-%m-%Y %I:%M %p",

        "DD-MM-YYYY hh:mm:ss AM":
            "%d-%m-%Y %I:%M:%S %p",

    }


    selected_format = formats.get(
        format_code,
        "%Y-%m-%d %H:%M:%S",
    )


    return value.strftime(
        selected_format
    )