from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.engine import get_db
from app.schemas.binding_type import (
    BindingTypeCreate,
    BindingTypeUpdate,
    BindingTypeResponse,
)
from app.services.binding_type_service import BindingTypeService

router = APIRouter(
    prefix="/binding-types",
    tags=["Binding Type Master"],
)

service = BindingTypeService()


@router.post("/", response_model=BindingTypeResponse)
def create_binding_type(
    data: BindingTypeCreate,
    db: Session = Depends(get_db),
):
    try:
        return service.create(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[BindingTypeResponse])
def get_binding_types(
    db: Session = Depends(get_db),
):
    return service.get_all(db)


@router.get("/{binding_type_id}", response_model=BindingTypeResponse)
def get_binding_type(
    binding_type_id: int,
    db: Session = Depends(get_db),
):
    try:
        return service.get_by_id(db, binding_type_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{binding_type_id}", response_model=BindingTypeResponse)
def update_binding_type(
    binding_type_id: int,
    data: BindingTypeUpdate,
    db: Session = Depends(get_db),
):
    try:
        return service.update(db, binding_type_id, data)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{binding_type_id}")
def delete_binding_type(
    binding_type_id: int,
    db: Session = Depends(get_db),
):
    try:
        return service.delete(db, binding_type_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))