"""
MKPrintingMasterPro ERP

Production Operation Execution Status History Repository

Build-035
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.production_operation_execution_status_history import (
    ProductionOperationExecutionStatusHistory,
)


class ProductionOperationExecutionStatusHistoryRepository:
    """
    Repository for Production Operation Execution Status History.
    """

    def get_by_execution(
        self,
        db: Session,
        execution_id: int,
    ):
        statement = (
            select(
                ProductionOperationExecutionStatusHistory
            )
            .where(
                ProductionOperationExecutionStatusHistory
                .production_operation_execution_id
                == execution_id
            )
            .order_by(
                ProductionOperationExecutionStatusHistory.id
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
            ProductionOperationExecutionStatusHistory,
            history_id,
        )

    def create(
        self,
        db: Session,
        history: ProductionOperationExecutionStatusHistory,
    ):
        db.add(history)
        db.flush()
        db.refresh(history)

        return history

    def delete(
        self,
        db: Session,
        history: ProductionOperationExecutionStatusHistory,
    ):
        db.delete(history)
        db.flush()
