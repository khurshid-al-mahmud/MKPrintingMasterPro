"""
MKPrintingMasterPro ERP

Operation Master Service

Build-031
"""

from sqlalchemy.orm import Session

from app.models.operation_master import OperationMaster
from app.repositories.operation_master import (
    OperationMasterRepository,
)


class OperationMasterService:
    """
    Service layer for Operation Master.
    """

    def __init__(self, db: Session):
        self.db = db
        self.repository = OperationMasterRepository(db)

    # ======================================================
    # Get by ID
    # ======================================================

    def get_by_id(
        self,
        operation_id: int,
    ) -> OperationMaster | None:

        return self.repository.get_by_id(
            operation_id
        )

    # ======================================================
    # Get by Code
    # ======================================================

    def get_by_code(
        self,
        operation_code: str,
    ) -> OperationMaster | None:

        return self.repository.get_by_code(
            operation_code
        )

    # ======================================================
    # Get by Name
    # ======================================================

    def get_by_name(
        self,
        operation_name: str,
    ) -> OperationMaster | None:

        return self.repository.get_by_name(
            operation_name
        )

    # ======================================================
    # Get All
    # ======================================================

    def get_all(
        self,
    ) -> list[OperationMaster]:

        return self.repository.get_all()

    # ======================================================
    # Get Active
    # ======================================================

    def get_active(
        self,
    ) -> list[OperationMaster]:

        return self.repository.get_active()

    # ======================================================
    # Create
    # ======================================================

    def create(
        self,
        operation_code: str,
        operation_name: str,
        description: str | None = None,
        display_order: int = 1,
        is_active: bool = True,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> OperationMaster:

        # --------------------------------------------------
        # Duplicate Code Check
        # --------------------------------------------------

        existing_by_code = (
            self.repository.get_by_code(
                operation_code
            )
        )

        if existing_by_code is not None:
            raise ValueError(
                "Operation Code already exists."
            )

        # --------------------------------------------------
        # Duplicate Name Check
        # --------------------------------------------------

        existing_by_name = (
            self.repository.get_by_name(
                operation_name
            )
        )

        if existing_by_name is not None:
            raise ValueError(
                "Operation Name already exists."
            )

        # --------------------------------------------------
        # Create Model
        # --------------------------------------------------

        operation = OperationMaster(
            operation_code=operation_code,
            operation_name=operation_name,
            description=description,
            display_order=display_order,
            is_active=is_active,
            created_by=created_by,
            updated_by=updated_by,
        )

        return self.repository.create(
            operation
        )

    # ======================================================
    # Update
    # ======================================================

    def update(
        self,
        operation_id: int,
        operation_code: str | None = None,
        operation_name: str | None = None,
        description: str | None = None,
        display_order: int | None = None,
        is_active: bool | None = None,
        updated_by: str | None = None,
    ) -> OperationMaster:

        # --------------------------------------------------
        # Find Operation
        # --------------------------------------------------

        operation = self.repository.get_by_id(
            operation_id
        )

        if operation is None:
            raise ValueError(
                "Operation not found."
            )

        # --------------------------------------------------
        # Code Change
        # --------------------------------------------------

        if (
            operation_code is not None
            and operation_code
            != operation.operation_code
        ):

            existing_by_code = (
                self.repository.get_by_code(
                    operation_code
                )
            )

            if existing_by_code is not None:
                raise ValueError(
                    "Operation Code already exists."
                )

            operation.operation_code = (
                operation_code
            )

        # --------------------------------------------------
        # Name Change
        # --------------------------------------------------

        if (
            operation_name is not None
            and operation_name
            != operation.operation_name
        ):

            existing_by_name = (
                self.repository.get_by_name(
                    operation_name
                )
            )

            if existing_by_name is not None:
                raise ValueError(
                    "Operation Name already exists."
                )

            operation.operation_name = (
                operation_name
            )

        # --------------------------------------------------
        # Other Fields
        # --------------------------------------------------

        if description is not None:
            operation.description = description

        if display_order is not None:
            operation.display_order = display_order

        if is_active is not None:
            operation.is_active = is_active

        if updated_by is not None:
            operation.updated_by = updated_by

        return self.repository.update(
            operation
        )

    # ======================================================
    # Delete
    # ======================================================

    def delete(
        self,
        operation_id: int,
    ) -> None:

        operation = self.repository.get_by_id(
            operation_id
        )

        if operation is None:
            raise ValueError(
                "Operation not found."
            )

        self.repository.delete(
            operation
        )