"""
Employee Repository.

Database access layer
for Employee Management.
"""

from sqlalchemy import or_

from app.models.employee_profile import EmployeeProfile
from app.models.party import Party


class EmployeeRepository:
    """
    Repository for Employee Profile.
    """

    def __init__(
        self,
        db,
    ):
        self.db = db

    def create(
        self,
        employee: EmployeeProfile,
    ) -> EmployeeProfile:

        self.db.add(
            employee,
        )

        self.db.commit()

        self.db.refresh(
            employee,
        )

        return employee

    def get_by_id(
        self,
        employee_id: int,
    ) -> EmployeeProfile | None:

        return (
            self.db.query(
                EmployeeProfile,
            )
            .filter(
                EmployeeProfile.id == employee_id,
                EmployeeProfile.is_active == True,
            )
            .first()
        )

    def get_all(
        self,
    ) -> list[EmployeeProfile]:

        return (
            self.db.query(
                EmployeeProfile,
            )
            .filter(
                EmployeeProfile.is_active == True,
            )
            .all()
        )

    def update(
        self,
        employee_id: int,
        employee_data: dict,
    ) -> EmployeeProfile | None:

        employee = self.get_by_id(
            employee_id,
        )

        if employee is None:
            return None

        for key, value in employee_data.items():
            setattr(
                employee,
                key,
                value,
            )

        self.db.commit()

        self.db.refresh(
            employee,
        )

        return employee

    def soft_delete(
        self,
        employee_id: int,
    ) -> bool:

        employee = self.get_by_id(
            employee_id,
        )

        if employee is None:
            return False

        employee.is_active = False

        self.db.commit()

        return True

    def search(
        self,
        keyword: str,
    ) -> list[EmployeeProfile]:

        return (
            self.db.query(
                EmployeeProfile,
            )
            .join(
                Party,
                EmployeeProfile.party_id == Party.id,
            )
            .filter(
                EmployeeProfile.is_active == True,
            )
            .filter(
                or_(
                    Party.party_name.ilike(
                        f"%{keyword}%",
                    ),
                    Party.mobile.ilike(
                        f"%{keyword}%",
                    ),
                )
            )
            .all()
        )