"""
MKPrintingMasterPro ERP

Production Output Repository

Build-034 + Build-036
"""

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.production_operation_execution import (
    ProductionOperationExecution,
)
from app.models.production_output import ProductionOutput

from app.schemas.production_output import (
    ProductionOutputCreate,
    ProductionOutputUpdate,
)


class ProductionOutputRepository:
    """
    Repository for Production Output operations.

    Build-036:
        Production Output changes automatically synchronize
        the related Production Operation Execution quantities.
    """

    # ============================================================
    # Create
    # ============================================================

    def create(
        self,
        db: Session,
        data: ProductionOutputCreate,
    ) -> ProductionOutput:

        execution = (
            db.query(ProductionOperationExecution)
            .filter(
                ProductionOperationExecution.id
                == data.production_operation_execution_id
            )
            .first()
        )

        if not execution:
            raise ValueError(
                "Production Operation Execution not found"
            )

        production_output = ProductionOutput(
            **data.model_dump()
        )

        db.add(production_output)
        db.flush()

        self._sync_execution_quantities(
            db,
            data.production_operation_execution_id,
        )

        db.commit()
        db.refresh(production_output)

        return production_output

    # ============================================================
    # Get By ID
    # ============================================================

    def get_by_id(
        self,
        db: Session,
        output_id: int,
    ) -> ProductionOutput | None:

        return (
            db.query(ProductionOutput)
            .filter(
                ProductionOutput.id == output_id
            )
            .first()
        )

    # ============================================================
    # Get All
    # ============================================================

    def get_all(
        self,
        db: Session,
    ) -> list[ProductionOutput]:

        return (
            db.query(ProductionOutput)
            .order_by(
                ProductionOutput.id.desc()
            )
            .all()
        )

    # ============================================================
    # Get By Execution
    # ============================================================

    def get_by_execution(
        self,
        db: Session,
        execution_id: int,
    ) -> list[ProductionOutput]:

        return (
            db.query(ProductionOutput)
            .filter(
                ProductionOutput.production_operation_execution_id
                == execution_id
            )
            .order_by(
                ProductionOutput.id
            )
            .all()
        )

    # ============================================================
    # Update
    # ============================================================

    def update(
        self,
        db: Session,
        production_output: ProductionOutput,
        data: ProductionOutputUpdate,
    ) -> ProductionOutput:

        execution_id = (
            production_output.production_operation_execution_id
        )

        update_data = data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                production_output,
                field,
                value,
            )

        db.flush()

        self._sync_execution_quantities(
            db,
            execution_id,
        )

        db.commit()
        db.refresh(production_output)

        return production_output

    # ============================================================
    # Delete
    # ============================================================

    def delete(
        self,
        db: Session,
        production_output: ProductionOutput,
    ) -> None:

        execution_id = (
            production_output.production_operation_execution_id
        )

        db.delete(production_output)
        db.flush()

        self._sync_execution_quantities(
            db,
            execution_id,
        )

        db.commit()

    # ============================================================
    # Synchronize Execution Quantities
    # ============================================================

    def _sync_execution_quantities(
        self,
        db: Session,
        execution_id: int,
    ) -> None:

        execution = (
            db.query(ProductionOperationExecution)
            .filter(
                ProductionOperationExecution.id
                == execution_id
            )
            .first()
        )

        if not execution:
            raise ValueError(
                "Production Operation Execution not found"
            )

        totals = (
            db.query(
                func.coalesce(
                    func.sum(
                        ProductionOutput.output_quantity
                    ),
                    0,
                ),
                func.coalesce(
                    func.sum(
                        ProductionOutput.reject_quantity
                    ),
                    0,
                ),
            )
            .filter(
                ProductionOutput.production_operation_execution_id
                == execution_id
            )
            .first()
        )

        # --------------------------------------------------------
        # Aggregate query normally returns one row.
        # Explicit guard keeps Pylance type checking satisfied.
        # --------------------------------------------------------

        if totals is None:
            completed_quantity = 0
            reject_quantity = 0
        else:
            completed_quantity = totals[0] or 0
            reject_quantity = totals[1] or 0

        execution.completed_quantity = completed_quantity
        execution.reject_quantity = reject_quantity

        db.flush()