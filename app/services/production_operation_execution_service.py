"""
MKPrintingMasterPro ERP

Production Operation Execution Service

Build-033 + Build-035
"""

from sqlalchemy.orm import Session

from app.models.production_operation_execution import (
    ProductionOperationExecution,
)

from app.repositories.production_operation_execution_repository import (
    ProductionOperationExecutionRepository,
)

from app.schemas.production_operation_execution import (
    ProductionOperationExecutionCreate,
    ProductionOperationExecutionUpdate,
)

from app.services.production_operation_execution_status_history_service import (
    ProductionOperationExecutionStatusHistoryService,
)


class ProductionOperationExecutionService:
    """
    Production Operation Execution Business Service.

    Build-035:
        Automatically creates status history
        when the execution status changes.
    """

    def __init__(self, db: Session):
        self.db = db
        self.repository = ProductionOperationExecutionRepository(db)
        self.history_service = (
            ProductionOperationExecutionStatusHistoryService()
        )

    # ==========================
    # Create
    # ==========================

    def create(
        self,
        data: ProductionOperationExecutionCreate,
    ) -> ProductionOperationExecution:

        execution = ProductionOperationExecution(
            **data.model_dump()
        )

        return self.repository.create(execution)

    # ==========================
    # Get By ID
    # ==========================

    def get_by_id(
        self,
        execution_id: int,
    ) -> ProductionOperationExecution | None:

        return self.repository.get_by_id(
            execution_id
        )

    # ==========================
    # Get All
    # ==========================

    def get_all(
        self,
    ) -> list[ProductionOperationExecution]:

        return self.repository.get_all()

    # ==========================
    # Update
    # ==========================

    def update(
        self,
        execution_id: int,
        data: ProductionOperationExecutionUpdate,
    ) -> ProductionOperationExecution | None:

        execution = self.repository.get_by_id(
            execution_id
        )

        if not execution:
            return None

        # ------------------------------------------
        # Capture previous status before update
        # ------------------------------------------

        previous_status = execution.status

        # ------------------------------------------
        # Prepare update data
        # ------------------------------------------

        update_data = data.model_dump(
            exclude_unset=True
        )

        # ------------------------------------------
        # Determine whether status is changing
        # ------------------------------------------

        new_status = update_data.get("status")

        status_changed = (
            new_status is not None
            and new_status != previous_status
        )

        # ------------------------------------------
        # Apply execution updates
        # ------------------------------------------

        for key, value in update_data.items():
            setattr(
                execution,
                key,
                value,
            )

        # ------------------------------------------
        # Build status history only when status changes
        # ------------------------------------------

        if status_changed:

            self.history_service.create(
                db=self.db,
                execution_id=execution.id,
                previous_status=previous_status,
                new_status=execution.status,
                completed_quantity=execution.completed_quantity,
                reject_quantity=execution.reject_quantity,
                operator_name=execution.operator_name,
                remarks=execution.remarks,
            )

        # ------------------------------------------
        # Commit execution update + status history
        # in the same transaction
        # ------------------------------------------

        self.db.commit()

        # ------------------------------------------
        # Refresh execution after commit
        # ------------------------------------------

        self.db.refresh(execution)

        return execution

    # ==========================
    # Delete
    # ==========================

    def delete(
        self,
        execution_id: int,
    ) -> bool:

        execution = self.repository.get_by_id(
            execution_id
        )

        if not execution:
            return False

        self.repository.delete(
            execution
        )

        return True


# ==========================
# Service Instance
# ==========================

def get_production_operation_execution_service(
    db: Session,
):

    return ProductionOperationExecutionService(db)