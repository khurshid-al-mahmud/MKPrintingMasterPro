from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class NumberSequence(BaseModel):
    """Stores running number sequences for ERP modules."""

    __tablename__ = "number_sequences"

    prefix: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False,
    )

    current_number: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    digit_length: Mapped[int] = mapped_column(
        Integer,
        default=6,
        nullable=False,
    )
