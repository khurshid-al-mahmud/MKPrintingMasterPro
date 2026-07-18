"""
Employee Pydantic Schemas.

Request and Response Models
for Employee API.
"""

from datetime import date
from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class EmployeeBase(BaseModel):
    """
    Common Employee Fields.
    """

    party_id: int
    employee_code: str
    designation: str | None = None
    department: str | None = None
    joining_date: date | None = None
    salary: float = 0
    employment_type: str | None = None


class EmployeeCreate(EmployeeBase):
    """
    Create Employee Schema.
    """

    pass


class EmployeeUpdate(BaseModel):
    """
    Update Employee Schema.
    """

    party_id: int | None = None
    employee_code: str | None = None
    designation: str | None = None
    department: str | None = None
    joining_date: date | None = None
    salary: float | None = None
    employment_type: str | None = None


class EmployeeResponse(EmployeeBase):
    """
    Employee Response Schema.
    """

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )