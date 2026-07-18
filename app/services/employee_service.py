"""
Employee Service.

Business Logic Layer
for Employee Management.
"""

from app.models.employee_profile import EmployeeProfile
from app.repositories.employee_repository import EmployeeRepository
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
)


class EmployeeService:
    """
    Service layer for Employee management.
    """

    def __init__(
        self,
        repository: EmployeeRepository,
    ) -> None:
        self.repository = repository

    def create(
        self,
        employee: EmployeeCreate,
    ) -> EmployeeProfile:
        """
        Create employee.
        """

        new_employee = EmployeeProfile(
            party_id=employee.party_id,
            employee_code=employee.employee_code,
            designation=employee.designation,
            department=employee.department,
            joining_date=employee.joining_date,
            salary=employee.salary,
            employment_type=employee.employment_type,
        )

        return self.repository.create(
            new_employee,
        )

    def get_by_id(
        self,
        employee_id: int,
    ) -> EmployeeProfile | None:
        """
        Get employee by ID.
        """

        return self.repository.get_by_id(
            employee_id,
        )

    def get_all(
        self,
    ) -> list[EmployeeProfile]:
        """
        Get all employees.
        """

        return self.repository.get_all()

    def update(
        self,
        employee_id: int,
        employee_data: EmployeeUpdate,
    ) -> EmployeeProfile | None:
        """
        Update employee.
        """

        return self.repository.update(
            employee_id,
            employee_data.model_dump(
                exclude_unset=True,
            ),
        )

    def delete(
        self,
        employee_id: int,
    ) -> bool:
        """
        Soft delete employee.
        """

        return self.repository.soft_delete(
            employee_id,
        )

    def search(
        self,
        keyword: str,
    ) -> list[EmployeeProfile]:
        """
        Search employees.
        """

        return self.repository.search(
            keyword,
        )