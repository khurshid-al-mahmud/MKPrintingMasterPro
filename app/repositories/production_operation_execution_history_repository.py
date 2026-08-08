"""
MKPrintingMasterPro ERP

Production Operation Execution History Repository

Build-035
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.production_operation_execution_history import (
    ProductionOperationExecutionHistory,
)


class ProductionOperationExecutionHistoryRepository:
    """
    Repository for Production Operation Execution History.
    """

    def get_by_execution(
        self,
        db: Session,
        execution_id: int,
    ):
        statement = (
            select(
                ProductionOperationExecutionHistory
            )
            .where(
                ProductionOperationExecutionHistory
                .production_operation_execution_id
                == execution_id
            )
            .order_by(
                ProductionOperationExecutionHistory.id
            )
        )

        return list(
            db.scalars(statement).all()
        )

    def get_by_id(
        self,
        db: Session,
        history_id: int,
    ):
        return db.get(
            ProductionOperationExecutionHistory,
            history_id,
        )

    def create(
        self,
        db: Session,
        history: ProductionOperationExecutionHistory,
    ):
        db.add(history)
        db.flush()
        db.refresh(history)

        return history

    def delete(
        self,
        db: Session,
        history: ProductionOperationExecutionHistory,
    ):
        db.delete(history)
        db.flush()
