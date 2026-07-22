"""
System Setting Service.

Business Logic Layer
for System Setting Master.
"""

from app.repositories.system_setting_repository import (
    SystemSettingRepository,
)
from app.schemas.system_setting import (
    SystemSettingCreate,
    SystemSettingUpdate,
)


class SystemSettingService:
    """System Setting Service."""

    def __init__(
        self,
        repository: SystemSettingRepository,
    ):
        self.repository = repository

    def create(
        self,
        setting: SystemSettingCreate,
    ):

        existing = self.repository.get_by_key(
            setting.setting_key
        )

        if existing:
            raise ValueError(
                "Setting Key already exists."
            )

        return self.repository.create(setting)

    def get_all(self):

        return self.repository.get_all()

    def get_active(self):

        return self.repository.get_active()

    def get_by_id(
        self,
        setting_id: int,
    ):

        db_setting = self.repository.get_by_id(
            setting_id
        )

        if not db_setting:
            raise ValueError(
                "System Setting not found."
            )

        return db_setting

    def get_by_key(
        self,
        setting_key: str,
    ):

        db_setting = self.repository.get_by_key(
            setting_key
        )

        if not db_setting:
            raise ValueError(
                "System Setting not found."
            )

        return db_setting

    def update(
        self,
        setting_id: int,
        setting: SystemSettingUpdate,
    ):

        db_setting = self.repository.get_by_id(
            setting_id
        )

        if not db_setting:
            raise ValueError(
                "System Setting not found."
            )

        return self.repository.update(
            db_setting,
            setting,
        )

    def delete(
        self,
        setting_id: int,
    ):

        db_setting = self.repository.get_by_id(
            setting_id
        )

        if not db_setting:
            raise ValueError(
                "System Setting not found."
            )

        self.repository.delete(
            db_setting
        )

    def search(
        self,
        keyword: str,
    ):

        return self.repository.search(
            keyword
        )