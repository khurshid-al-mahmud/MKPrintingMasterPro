"""
MKPrintingMasterPro ERP

Operation Master Repository

Build-031
"""

from sqlalchemy.orm import Session

from app.models.operation_master import OperationMaster


class OperationMasterRepository:
    """
    Repository for Operation Master.
    """

    def __init__(self, db: Session):
        self.db = db

    # ======================================================
    # Get by ID
    # ======================================================

    def get_by_id(
        self,
        operation_id: int,
    ) -> OperationMaster | None:

        return (
            self.db.query(OperationMaster)
            .filter(
                OperationMaster.id == operation_id
            )
            .first()
        )

    # ======================================================
    # Get by Code
    # ======================================================

    def get_by_code(
        self,
        operation_code: str,
    ) -> OperationMaster | None:

        return (
            self.db.query(OperationMaster)
            .filter(
                OperationMaster.operation_code
                == operation_code
            )
            .first()
        )

    # ======================================================
    # Get by Name
    # ======================================================

    def get_by_name(
        self,
        operation_name: str,
    ) -> OperationMaster | None:

        return (
            self.db.query(OperationMaster)
            .filter(
                OperationMaster.operation_name
                == operation_name
            )
            .first()
        )

    # ======================================================
    # Get All
    # ======================================================

    def get_all(
        self,
    ) -> list[OperationMaster]:

        return (
            self.db.query(OperationMaster)
            .order_by(
                OperationMaster.display_order.asc(),
                OperationMaster.id.asc(),
            )
            .all()
        )

    # ======================================================
    # Get Active Operations
    # ======================================================

    def get_active(
        self,
    ) -> list[OperationMaster]:

        return (
            self.db.query(OperationMaster)
            .filter(
                OperationMaster.is_active.is_(True)
            )
            .order_by(
                OperationMaster.display_order.asc(),
                OperationMaster.id.asc(),
            )
            .all()
        )

    # ======================================================
    # Create
    # ======================================================

    def create(
        self,
        operation: OperationMaster,
    ) -> OperationMaster:

        try:
            self.db.add(operation)

            self.db.commit()

            self.db.refresh(operation)

            return operation

        except Exception:
            self.db.rollback()
            raise

    # ======================================================
    # Update
    # ======================================================

    def update(
        self,
        operation: OperationMaster,
    ) -> OperationMaster:

        try:
            self.db.add(operation)

            self.db.commit()

            self.db.refresh(operation)

            return operation

        except Exception:
            self.db.rollback()
            raise

    # ======================================================
    # Delete
    # ======================================================

    def delete(
        self,
        operation: OperationMaster,
    ) -> None:

        try:
            self.db.delete(operation)

            self.db.commit()

        except Exception:
            self.db.rollback()
            raise