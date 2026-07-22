"""
System Setting API.

REST API endpoints
for System Setting Master.
"""

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db

from app.repositories.system_setting_repository import (
    SystemSettingRepository,
)

from app.services.system_setting_service import (
    SystemSettingService,
)

from app.schemas.system_setting import (
    SystemSettingCreate,
    SystemSettingUpdate,
)

router = APIRouter(
    prefix="/system-settings",
    tags=["System Settings"],
)


def get_service(
    db: Session = Depends(get_db),
) -> SystemSettingService:
    repository = SystemSettingRepository(db)
    return SystemSettingService(repository)


@router.post("/")
def create_system_setting(
    data: SystemSettingCreate,
    service: SystemSettingService = Depends(get_service),
):
    return service.create(data)


@router.get("/")
def get_all_system_settings(
    service: SystemSettingService = Depends(get_service),
):
    return service.get_all()


@router.get("/{setting_id}")
def get_system_setting(
    setting_id: int,
    service: SystemSettingService = Depends(get_service),
):
    return service.get_by_id(setting_id)


@router.get("/key/{setting_key}")
def get_system_setting_by_key(
    setting_key: str,
    service: SystemSettingService = Depends(get_service),
):
    return service.get_by_key(setting_key)


@router.put("/{setting_id}")
def update_system_setting(
    setting_id: int,
    data: SystemSettingUpdate,
    service: SystemSettingService = Depends(get_service),
):
    return service.update(
        setting_id,
        data,
    )


@router.delete("/{setting_id}")
def delete_system_setting(
    setting_id: int,
    service: SystemSettingService = Depends(get_service),
):
    service.delete(setting_id)

    return {
        "message": "System Setting deleted successfully."
    }