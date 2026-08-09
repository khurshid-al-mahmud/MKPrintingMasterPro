"""
MKPrintingMasterPro ERP

Production Operation Execution Service

Build-033 + Build-035 + Build-038
"""

from sqlalchemy.orm import Session

from app.models.production_operation_execution import (
    ProductionOperationExecution,
)

from app.models.operation_assignment import (
    OperationAssignment,
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
    Business service for Production Operation Execution.

    Build-033:
        Core production operation execution.

    Build-035:
        Automatically records status changes
        in Production Operation Execution Status History.

    Build-038:
        Automatically synchronizes Operation Assignment
        when an execution is completed.
    """

    def __init__(self, db: Session):
        self.db = db

        self.repository = ProductionOperationExecutionRepository(
            db
        )

        self.history_service = (
            ProductionOperationExecutionStatusHistoryService()
        )

    # ============================================================
    # CREATE
    # ============================================================

    def create(
        self,
        data: ProductionOperationExecutionCreate,
    ) -> ProductionOperationExecution:

        execution = ProductionOperationExecution(
            **data.model_dump()
        )

        return self.repository.create(
            execution
        )

    # ============================================================
    # GET BY ID
    # ============================================================

    def get_by_id(
        self,
        execution_id: int,
    ) -> ProductionOperationExecution | None:

        return self.repository.get_by_id(
            execution_id
        )

    # ============================================================
    # GET ALL
    # ============================================================

    def get_all(
        self,
    ) -> list[ProductionOperationExecution]:

        return self.repository.get_all()

    # ============================================================
    # UPDATE
    # ============================================================

    def update(
        self,
        execution_id: int,
        data: ProductionOperationExecutionUpdate,
    ) -> ProductionOperationExecution | None:

        execution = self.repository.get_by_id(
            execution_id
        )

        if execution is None:
            return None

        # --------------------------------------------------------
        # Capture existing status BEFORE applying updates
        # --------------------------------------------------------

        previous_status = execution.status

        # --------------------------------------------------------
        # Convert Pydantic update schema to dictionary
        # --------------------------------------------------------

        update_data = data.model_dump(
            exclude_unset=True
        )

        # --------------------------------------------------------
        # Determine whether status is changing
        # --------------------------------------------------------

        new_status = update_data.get(
            "status"
        )

        status_changed = (
            new_status is not None
            and new_status != previous_status
        )

        # --------------------------------------------------------
        # Apply execution updates
        # --------------------------------------------------------

        for key, value in update_data.items():
            setattr(
                execution,
                key,
                value,
            )

        # --------------------------------------------------------
        # Create status history when status changes
        # --------------------------------------------------------

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

        # --------------------------------------------------------
        # Build-038
        #
        # When execution becomes Completed, synchronize the
        # related Operation Assignment in the SAME transaction.
        # --------------------------------------------------------

        if (
            status_changed
            and execution.status == "Completed"
        ):

            assignment = (
                self.db.query(OperationAssignment)
                .filter(
                    OperationAssignment.id
                    == execution.operation_assignment_id
                )
                .first()
            )

            if assignment is not None:

                assignment.status = "Completed"
                assignment.is_completed = True

                if execution.operator_name:
                    assignment.updated_by = (
                        execution.operator_name
                    )

        # --------------------------------------------------------
        # Commit execution, history and assignment update
        # in the SAME database transaction
        # --------------------------------------------------------

        self.db.commit()

        # --------------------------------------------------------
        # Refresh execution after commit
        # --------------------------------------------------------

        self.db.refresh(
            execution
        )

        return execution

    # ============================================================
    # DELETE
    # ============================================================

    def delete(
        self,
        execution_id: int,
    ) -> bool:

        execution = self.repository.get_by_id(
            execution_id
        )

        if execution is None:
            return False

        self.repository.delete(
            execution
        )

        return True


# ================================================================
# SERVICE FACTORY
# ================================================================

def get_production_operation_execution_service(
    db: Session,
) -> ProductionOperationExecutionService:

    return ProductionOperationExecutionService(
        db
    )
