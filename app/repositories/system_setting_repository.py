"""
System Setting Repository.

Database operations for
System Setting Master.
"""

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.system_setting import SystemSetting
from app.schemas.system_setting import (
    SystemSettingCreate,
    SystemSettingUpdate,
)


class SystemSettingRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        setting: SystemSettingCreate,
    ) -> SystemSetting:

        db_setting = SystemSetting(
            **setting.model_dump()
        )

        self.db.add(db_setting)
        self.db.commit()
        self.db.refresh(db_setting)

        return db_setting

    def get_all(self):

        return (
            self.db.query(SystemSetting)
            .order_by(
                SystemSetting.setting_key,
            )
            .all()
        )

    def get_active(self):

        return (
            self.db.query(SystemSetting)
            .filter(
                SystemSetting.is_active.is_(True)
            )
            .order_by(
                SystemSetting.setting_key,
            )
            .all()
        )

    def get_by_id(
        self,
        setting_id: int,
    ):

        return (
            self.db.query(SystemSetting)
            .filter(
                SystemSetting.id == setting_id
            )
            .first()
        )

    def get_by_key(
        self,
        setting_key: str,
    ):

        return (
            self.db.query(SystemSetting)
            .filter(
                SystemSetting.setting_key == setting_key
            )
            .first()
        )

    def update(
        self,
        db_setting: SystemSetting,
        setting: SystemSettingUpdate,
    ):

        update_data = setting.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_setting,
                key,
                value,
            )

        self.db.commit()
        self.db.refresh(db_setting)

        return db_setting

    def delete(
        self,
        db_setting: SystemSetting,
    ):

        self.db.delete(db_setting)
        self.db.commit()

    def search(
        self,
        keyword: str,
    ):

        return (
            self.db.query(SystemSetting)
            .filter(
                or_(
                    SystemSetting.setting_key.ilike(
                        f"%{keyword}%"
                    ),
                    SystemSetting.description.ilike(
                        f"%{keyword}%"
                    ),
                )
            )
            .order_by(
                SystemSetting.setting_key,
            )
            .all()
        )