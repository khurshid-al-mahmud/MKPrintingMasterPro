"""
MKPrintingMasterPro ERP

Production Operation Execution Repository

Build-033

Repository layer for tracking
production operation execution.
"""

from sqlalchemy.orm import Session

from app.models.production_operation_execution import (
    ProductionOperationExecution,
)

from app.repositories.base_repository import BaseRepository


class ProductionOperationExecutionRepository(
    BaseRepository
):
    """
    Production Operation Execution Repository.
    """

    def __init__(self, db: Session):
        super().__init__(
            db,
            ProductionOperationExecution,
        )

    # =====================================
    # Get By Production Order
    # =====================================

    def get_by_production_order(
        self,
        production_order_id: int,
    ):
        return (
            self.db.query(
                ProductionOperationExecution
            )
            .filter(
                ProductionOperationExecution.production_order_id
                == production_order_id
            )
            .order_by(
                ProductionOperationExecution.id
            )
            .all()
        )

    # =====================================
    # Get By Operation Assignment
    # =====================================

    def get_by_operation_assignment(
        self,
        operation_assignment_id: int,
    ):
        return (
            self.db.query(
                ProductionOperationExecution
            )
            .filter(
                ProductionOperationExecution.operation_assignment_id
                == operation_assignment_id
            )
            .first()
        )

    # =====================================
    # Get Running Operations
    # =====================================

    def get_running_operations(self):
        return (
            self.db.query(
                ProductionOperationExecution
            )
            .filter(
                ProductionOperationExecution.status
                == "Running"
            )
            .all()
        )

    # =====================================
    # Get Completed Operations
    # =====================================

    def get_completed_operations(
        self,
    ):
        return (
            self.db.query(
                ProductionOperationExecution
            )
            .filter(
                ProductionOperationExecution.status
                == "Completed"
            )
            .all()
        )


# Repository Object

production_operation_execution_repository = (
    ProductionOperationExecutionRepository
)