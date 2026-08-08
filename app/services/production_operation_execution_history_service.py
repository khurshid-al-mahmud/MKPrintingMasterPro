"""
MKPrintingMasterPro ERP

Production Operation Execution History Service

Build-035
"""

from sqlalchemy.orm import Session

from app.models.production_operation_execution_history import (
    ProductionOperationExecutionHistory,
)

from app.repositories.production_operation_execution_history_repository import (
    ProductionOperationExecutionHistoryRepository,
)


class ProductionOperationExecutionHistoryService:
    """
    Business service for Production Operation Execution History.
    """

    def __init__(self):
        self.repository = ProductionOperationExecutionHistoryRepository()

    # ============================================================
    # Get History By Execution
    # ============================================================

    def get_by_execution(
        self,
        db: Session,
        execution_id: int,
    ) -> list[ProductionOperationExecutionHistory]:

        return self.repository.get_by_execution(
            db,
            execution_id,
        )

    # ============================================================
    # Get History By ID
    # ============================================================

    def get_by_id(
        self,
        db: Session,
        history_id: int,
    ) -> ProductionOperationExecutionHistory | None:

        return self.repository.get_by_id(
            db,
            history_id,
        )

    # ============================================================
    # Create History
    # ============================================================

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
    ) -> ProductionOperationExecutionHistory:

        history = ProductionOperationExecutionHistory(
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

    # ============================================================
    # Delete History
    # ============================================================

    def delete(
        self,
        db: Session,
        history_id: int,
    ) -> bool:

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