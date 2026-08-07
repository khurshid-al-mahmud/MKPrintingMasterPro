"""
MKPrintingMasterPro ERP

Job Order Repository

Build-030
"""

from sqlalchemy.orm import Session

from app.models.job_order_master import JobOrderMaster


class JobOrderRepository:
    """
    Job Order Repository.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        job_order: JobOrderMaster,
    ):
        self.db.add(job_order)
        self.db.commit()
        self.db.refresh(job_order)
        return job_order

    def get_by_id(
        self,
        job_order_id: int,
    ):
        return (
            self.db.query(JobOrderMaster)
            .filter(
                JobOrderMaster.id == job_order_id
            )
            .first()
        )

    def get_all(self):
        return (
            self.db.query(JobOrderMaster)
            .all()
        )

    def update(
        self,
        job_order: JobOrderMaster,
    ):
        self.db.commit()
        self.db.refresh(job_order)
        return job_order

    def delete(
        self,
        job_order: JobOrderMaster,
    ):
        self.db.delete(job_order)
        self.db.commit()