"""
MKPrintingMasterPro ERP

Job Order Status History Model
Build-030 Phase-6 Step-3
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database.base import Base


class JobOrderStatusHistory(Base):

    __tablename__ = "job_order_status_history"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    job_order_id = Column(
        Integer,
        ForeignKey("job_order_master.id"),
        nullable=False
    )


    old_status = Column(
        String(50),
        nullable=True
    )


    new_status = Column(
        String(50),
        nullable=False
    )


    changed_by = Column(
        String(100),
        nullable=True
    )


    remarks = Column(
        String(255),
        nullable=True
    )


    changed_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )