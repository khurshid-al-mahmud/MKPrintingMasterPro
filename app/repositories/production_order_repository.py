"""
MKPrintingMasterPro ERP

Production Order Repository

Build-031
"""

from sqlalchemy.orm import Session

from app.models.production_order_master import ProductionOrderMaster


class ProductionOrderRepository:
    """
    Repository for Production Order Master.
    """

    def __init__(self, db: Session):
        self.db = db

    # ======================================================
    # Get by ID
    # ======================================================

    def get_by_id(
        self,
        production_order_id: int,
    ) -> ProductionOrderMaster | None:

        return (
            self.db.query(ProductionOrderMaster)
            .filter(
                ProductionOrderMaster.id == production_order_id
            )
            .first()
        )

    # ======================================================
    # Get by Production Order No
    # ======================================================

    def get_by_no(
        self,
        production_order_no: str,
    ) -> ProductionOrderMaster | None:

        return (
            self.db.query(ProductionOrderMaster)
            .filter(
                ProductionOrderMaster.production_order_no
                == production_order_no
            )
            .first()
        )

    # ======================================================
    # Get by Job Order
    # ======================================================

    def get_by_job_order(
        self,
        job_order_id: int,
    ) -> list[ProductionOrderMaster]:

        return (
            self.db.query(ProductionOrderMaster)
            .filter(
                ProductionOrderMaster.job_order_id
                == job_order_id
            )
            .order_by(
                ProductionOrderMaster.id.asc()
            )
            .all()
        )

    # ======================================================
    # Get All
    # ======================================================

    def get_all(
        self,
    ) -> list[ProductionOrderMaster]:

        return (
            self.db.query(ProductionOrderMaster)
            .order_by(
                ProductionOrderMaster.id.desc()
            )
            .all()
        )

    # ======================================================
    # Create
    # ======================================================

    def create(
        self,
        production_order: ProductionOrderMaster,
    ) -> ProductionOrderMaster:

        self.db.add(production_order)

        self.db.flush()

        self.db.refresh(production_order)

        # IMPORTANT:
        # Permanently save Production Order
        self.db.commit()

        # Refresh after commit
        self.db.refresh(production_order)

        return production_order

    # ======================================================
    # Update
    # ======================================================

    def update(
        self,
        production_order: ProductionOrderMaster,
    ) -> ProductionOrderMaster:

        self.db.add(production_order)

        self.db.flush()

        # Permanently save update
        self.db.commit()

        self.db.refresh(production_order)

        return production_order

    # ======================================================
    # Delete
    # ======================================================

    def delete(
        self,
        production_order: ProductionOrderMaster,
    ) -> None:

        self.db.delete(production_order)

        self.db.commit()