"""
MKPrintingMasterPro ERP

Production Output Model

Build-034
"""

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base


class ProductionOutput(Base):

    __tablename__ = "production_outputs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    production_operation_execution_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(
            "production_operation_executions.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    output_quantity: Mapped[float] = mapped_column(
        Numeric(18, 3),
        nullable=False
    )

    reject_quantity: Mapped[float | None] = mapped_column(
        Numeric(18, 3),
        nullable=True,
        default=0
    )

    output_status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="Completed"
    )

    operator_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow
    )


    # Relationship

    production_operation_execution = relationship(
        "ProductionOperationExecution",
        back_populates="production_outputs"
    )