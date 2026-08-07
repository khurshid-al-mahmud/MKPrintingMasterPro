"""
MKPrintingMasterPro ERP

Job Order Status History Service

Build-030 Phase-6
"""

from datetime import datetime

from app.models.job_order_status_history import (
    JobOrderStatusHistory
)


class JobOrderStatusHistoryService:
    """
    Service for Job Order Status History
    """

    def __init__(
        self,
        db
    ):

        self.db = db


    # =====================================
    # Create Status History
    # =====================================

    def create_history(
        self,
        job_order_id: int,
        old_status: str,
        new_status: str,
        changed_by: str = "Admin",
        remarks: str | None = None
    ):

        history = JobOrderStatusHistory(

            job_order_id=job_order_id,

            old_status=old_status,

            new_status=new_status,

            changed_by=changed_by,

            remarks=remarks,

            changed_at=datetime.now()

        )


        self.db.add(history)

        self.db.commit()

        self.db.refresh(history)


        return history



    # =====================================
    # Get History By Job Order
    # Build-030 Phase-6 Step-3.4
    # =====================================

    def get_history_by_job_order(
        self,
        job_order_id: int
    ):

        history = (

            self.db.query(
                JobOrderStatusHistory
            )

            .filter(
                JobOrderStatusHistory.job_order_id
                == job_order_id
            )

            .order_by(
                JobOrderStatusHistory.changed_at.asc()
            )

            .all()

        )


        return history