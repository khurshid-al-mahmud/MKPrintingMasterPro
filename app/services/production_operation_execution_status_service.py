"""
MKPrintingMasterPro ERP

Production Operation Execution Status Service

Build-035
"""

from sqlalchemy.orm import Session

from app.models.production_operation_execution_status import (
    ProductionOperationExecutionStatus,
)

from app.repositories.production_operation_execution_status_repository import (
    ProductionOperationExecutionStatusRepository,
)


class ProductionOperationExecutionStatusService:
    """
    Business service for Production Operation Execution Status.
    """

    def __init__(self):
        self.repository = ProductionOperationExecutionStatusRepository()

    # ============================================================
    # Get All Statuses
    # ============================================================

    def get_all(
        self,
        db: Session,
        active_only: bool = False,
    ) -> list[ProductionOperationExecutionStatus]:

        return self.repository.get_all(
            db,
            active_only=active_only,
        )

    # ============================================================
    # Get Status By ID
    # ============================================================

    def get_by_id(
        self,
        db: Session,
        status_id: int,
    ) -> ProductionOperationExecutionStatus | None:

        return self.repository.get_by_id(
            db,
            status_id,
        )

    # ============================================================
    # Get Status By Code
    # ============================================================

    def get_by_code(
        self,
        db: Session,
        status_code: str,
    ) -> ProductionOperationExecutionStatus | None:

        return self.repository.get_by_code(
            db,
            status_code,
        )

    # ============================================================
    # Create Status
    # ============================================================

    def create(
        self,
        db: Session,
        data,
    ) -> ProductionOperationExecutionStatus:

        status = ProductionOperationExecutionStatus(
            **data.model_dump()
        )

        return self.repository.create(
            db,
            status,
        )

    # ============================================================
    # Update Status
    # ============================================================

    def update(
        self,
        db: Session,
        status_id: int,
        data,
    ) -> ProductionOperationExecutionStatus | None:

        status = self.repository.get_by_id(
            db,
            status_id,
        )

        if not status:
            return None

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                status,
                field,
                value,
            )

        return self.repository.update(
            db,
            status,
        )

    # ============================================================
    # Delete Status
    # ============================================================

    def delete(
        self,
        db: Session,
        status_id: int,
    ) -> bool:

        status = self.repository.get_by_id(
            db,
            status_id,
        )

        if not status:
            return False

        self.repository.delete(
            db,
            status,
        )

        return True