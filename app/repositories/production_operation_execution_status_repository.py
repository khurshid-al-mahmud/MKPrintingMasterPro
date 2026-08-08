"""
MKPrintingMasterPro ERP

Production Operation Execution Status Repository

Build-035
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.production_operation_execution_status import (
    ProductionOperationExecutionStatus,
)


class ProductionOperationExecutionStatusRepository:
    """
    Repository for Production Operation Execution Status.
    """

    def get_all(
        self,
        db: Session,
        active_only: bool = False,
    ):
        statement = (
            select(ProductionOperationExecutionStatus)
            .order_by(
                ProductionOperationExecutionStatus.display_order,
                ProductionOperationExecutionStatus.id,
            )
        )

        if active_only:
            statement = statement.where(
                ProductionOperationExecutionStatus.is_active.is_(True)
            )

        return list(db.scalars(statement).all())

    def get_by_id(
        self,
        db: Session,
        status_id: int,
    ):
        return db.get(
            ProductionOperationExecutionStatus,
            status_id,
        )

    def get_by_code(
        self,
        db: Session,
        status_code: str,
    ):
        statement = select(
            ProductionOperationExecutionStatus
        ).where(
            ProductionOperationExecutionStatus.status_code
            == status_code
        )

        return db.scalar(statement)

    def create(
        self,
        db: Session,
        status: ProductionOperationExecutionStatus,
    ):
        db.add(status)
        db.flush()
        db.refresh(status)

        return status

    def update(
        self,
        db: Session,
        status: ProductionOperationExecutionStatus,
    ):
        db.flush()
        db.refresh(status)

        return status

    def delete(
        self,
        db: Session,
        status: ProductionOperationExecutionStatus,
    ):
        db.delete(status)
        db.flush()
