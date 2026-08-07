"""
Golden Date-Time Service.

Central Date-Time Service
for MKPrintingMasterPro ERP.

Supports:
- AUTO / MANUAL date
- DATE ONLY
- TIME ONLY
- DATE TIME
- System Setting Integration
"""

from datetime import date

from sqlalchemy.orm import Session

from app.repositories.system_setting_repository import (
    SystemSettingRepository,
)

from app.core.date_service import (
    get_date,
    get_time,
    get_datetime,
    resolve_document_date,
)


class DateTimeService:
    """
    ERP Central Date-Time Service.
    """

    def __init__(
        self,
        db: Session,
    ):

        self.repository = SystemSettingRepository(db)


    # ---------------------------------
    # Get System Setting
    # ---------------------------------

    def get_setting(
        self,
        key: str,
        default: str,
    ) -> str:
        """
        Get setting value by key.
        """

        setting = (
            self.repository
            .get_by_key(key)
        )


        if setting and setting.setting_value:
            return str(
                setting.setting_value
            )


        return default



    # ---------------------------------
    # Document Date AUTO / MANUAL
    # ---------------------------------

    def get_document_date(
        self,
        manual_date: date | None = None,
    ) -> date:
        """
        Resolve document date.
        """

        mode = self.get_setting(
            "default_date_mode",
            "AUTO",
        )


        return resolve_document_date(
            mode=mode,
            manual_date=manual_date,
        )



    # ---------------------------------
    # Date Only
    # ---------------------------------

    def get_display_date(
        self,
    ) -> str:
        """
        Return formatted date.
        """

        date_format = self.get_setting(
            "default_date_format",
            "YYYY-MM-DD",
        )


        return get_date(
            format_name=date_format,
        )



    # ---------------------------------
    # Time Only
    # ---------------------------------

    def get_display_time(
        self,
    ) -> str:
        """
        Return formatted time.
        """

        time_format = self.get_setting(
            "default_time_format",
            "24H",
        )


        return get_time(
            format_name=time_format,
        )



    # ---------------------------------
    # Date + Time
    # ---------------------------------

    def get_display_datetime(
        self,
    ) -> str:
        """
        Return formatted date and time.
        """

        date_format = self.get_setting(
            "default_date_format",
            "YYYY-MM-DD",
        )


        time_format = self.get_setting(
            "default_time_format",
            "24H",
        )


        return get_datetime(
            date_format=date_format,
            time_format=time_format,
        )