from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BindingTypeBase(BaseModel):
    binding_type_code: str
    binding_type_name: str
    display_order: int = 1
    is_active: bool = True


class BindingTypeCreate(BindingTypeBase):
    pass


class BindingTypeUpdate(BindingTypeBase):
    pass


class BindingTypeResponse(BindingTypeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)