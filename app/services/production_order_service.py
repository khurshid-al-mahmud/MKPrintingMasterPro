"""
MKPrintingMasterPro ERP

Production Order Service

Build-031
"""

from datetime import datetime

from sqlalchemy.orm import Session

from app.models.production_order_master import ProductionOrderMaster
from app.repositories.production_order_repository import (
    ProductionOrderRepository,
)


class ProductionOrderService:
    """
    Service layer for Production Order Master.
    """

    def __init__(self, db: Session):
        self.db = db
        self.repository = ProductionOrderRepository(db)

    def get_by_id(
        self,
        production_order_id: int,
    ) -> ProductionOrderMaster | None:
        return self.repository.get_by_id(
            production_order_id
        )

    def get_by_no(
        self,
        production_order_no: str,
    ) -> ProductionOrderMaster | None:
        return self.repository.get_by_no(
            production_order_no
        )

    def get_by_job_order(
        self,
        job_order_id: int,
    ) -> list[ProductionOrderMaster]:
        return self.repository.get_by_job_order(
            job_order_id
        )

    def get_all(
        self,
    ) -> list[ProductionOrderMaster]:
        return self.repository.get_all()

    def create(
        self,
        production_order_no: str,
        production_order_date: datetime,
        job_order_id: int,
        status: str = "Open",
        priority: str = "Normal",
        planned_start_date: datetime | None = None,
        planned_end_date: datetime | None = None,
        remarks: str | None = None,
        created_by: str | None = None,
        updated_by: str | None = None,
    ) -> ProductionOrderMaster:

        existing = self.repository.get_by_no(
            production_order_no
        )

        if existing is not None:
            raise ValueError(
                "Production Order No already exists."
            )

        production_order = ProductionOrderMaster(
            production_order_no=production_order_no,
            production_order_date=production_order_date,
            job_order_id=job_order_id,
            status=status,
            priority=priority,
            planned_start_date=planned_start_date,
            planned_end_date=planned_end_date,
            remarks=remarks,
            created_by=created_by,
            updated_by=updated_by,
        )

        return self.repository.create(
            production_order
        )

    def update(
        self,
        production_order_id: int,
        production_order_no: str | None = None,
        production_order_date: datetime | None = None,
        job_order_id: int | None = None,
        status: str | None = None,
        priority: str | None = None,
        planned_start_date: datetime | None = None,
        planned_end_date: datetime | None = None,
        remarks: str | None = None,
        updated_by: str | None = None,
    ) -> ProductionOrderMaster:

        production_order = self.repository.get_by_id(
            production_order_id
        )

        if production_order is None:
            raise ValueError(
                "Production Order not found."
            )

        if (
            production_order_no is not None
            and production_order_no
            != production_order.production_order_no
        ):
            existing = self.repository.get_by_no(
                production_order_no
            )

            if existing is not None:
                raise ValueError(
                    "Production Order No already exists."
                )

            production_order.production_order_no = (
                production_order_no
            )

        if production_order_date is not None:
            production_order.production_order_date = (
                production_order_date
            )

        if job_order_id is not None:
            production_order.job_order_id = job_order_id

        if status is not None:
            production_order.status = status

        if priority is not None:
            production_order.priority = priority

        if planned_start_date is not None:
            production_order.planned_start_date = (
                planned_start_date
            )

        if planned_end_date is not None:
            production_order.planned_end_date = (
                planned_end_date
            )

        if remarks is not None:
            production_order.remarks = remarks

        if updated_by is not None:
            production_order.updated_by = updated_by

        return self.repository.update(
            production_order
        )

    def delete(
        self,
        production_order_id: int,
    ) -> None:

        production_order = self.repository.get_by_id(
            production_order_id
        )

        if production_order is None:
            raise ValueError(
                "Production Order not found."
            )

        self.repository.delete(
            production_order
        )