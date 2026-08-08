"""
MKPrintingMasterPro ERP

Production Operation Execution Status History Service

Build-035
"""

from sqlalchemy.orm import Session

from app.models.production_operation_execution_status_history import (
    ProductionOperationExecutionStatusHistory,
)

from app.repositories.production_operation_execution_status_history_repository import (
    ProductionOperationExecutionStatusHistoryRepository,
)


class ProductionOperationExecutionStatusHistoryService:
    """
    Business service for Production Operation Execution Status History.
    """

    def __init__(self):
        self.repository = (
            ProductionOperationExecutionStatusHistoryRepository()
        )

    def get_by_execution(
        self,
        db: Session,
        execution_id: int,
    ):
        return self.repository.get_by_execution(
            db,
            execution_id,
        )

    def get_by_id(
        self,
        db: Session,
        history_id: int,
    ):
        return self.repository.get_by_id(
            db,
            history_id,
        )

    def create(
        self,
        db: Session,
        execution_id: int,
        previous_status: str | None,
        new_status: str,
        completed_quantity: float | None = None,
        reject_quantity: float | None = None,
        operator_name: str | None = None,
        remarks: str | None = None,
    ):
        history = ProductionOperationExecutionStatusHistory(
            production_operation_execution_id=execution_id,
            previous_status=previous_status,
            new_status=new_status,
            completed_quantity=completed_quantity,
            reject_quantity=reject_quantity,
            operator_name=operator_name,
            remarks=remarks,
        )

        return self.repository.create(
            db,
            history,
        )

    def delete(
        self,
        db: Session,
        history_id: int,
    ):
        history = self.repository.get_by_id(
            db,
            history_id,
        )

        if not history:
            return False

        self.repository.delete(
            db,
            history,
        )

        return True
