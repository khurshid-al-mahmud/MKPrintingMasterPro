from sqlalchemy.orm import Session

from app.models.job_order_status_history import JobOrderStatusHistory


class JobOrderStatusHistoryRepository:

    def __init__(self, db: Session):
        self.db = db


    def create(
        self,
        job_order_id: int,
        old_status: str,
        new_status: str,
        changed_by: str | None = None,
        remarks: str | None = None
    ):

        history = JobOrderStatusHistory(
            job_order_id=job_order_id,
            old_status=old_status,
            new_status=new_status,
            changed_by=changed_by,
            remarks=remarks
        )

        self.db.add(history)
        self.db.commit()
        self.db.refresh(history)

        return history


    def get_by_job_order_id(
        self,
        job_order_id: int
    ):

        return (
            self.db.query(JobOrderStatusHistory)
            .filter(
                JobOrderStatusHistory.job_order_id == job_order_id
            )
            .order_by(
                JobOrderStatusHistory.changed_at.desc()
            )
            .all()
        )