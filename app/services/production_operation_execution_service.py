"""
MKPrintingMasterPro ERP

Production Operation Execution Service

Build-033
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


class ProductionOperationExecutionService:
    """
    Production Operation Execution Business Service.
    """

    def __init__(self, db: Session):
        self.repository = ProductionOperationExecutionRepository(db)


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

        return self.repository.get_by_id(execution_id)


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


        update_data = data.model_dump(
            exclude_unset=True
        )


        for key, value in update_data.items():
            setattr(
                execution,
                key,
                value,
            )


        return self.repository.update(
            execution
        )


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