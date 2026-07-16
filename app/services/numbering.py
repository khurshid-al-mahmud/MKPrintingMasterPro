"""
Global Number Generator Service.

This service is responsible for generating
Customer, Supplier, Employee, Invoice,
Quotation and other running numbers.
"""

from sqlalchemy.orm import Session

from app.models.number_sequence import NumberSequence


class NumberingService:
    """ERP Global Number Generator."""

    def __init__(self, db: Session):
        self.db = db

    def generate_next_number(self, prefix: str) -> str:
        """Generate the next running number."""

        sequence = (
            self.db.query(NumberSequence)
            .filter(NumberSequence.prefix == prefix)
            .first()
        )

        if sequence is None:
            raise ValueError(
                f"Number sequence '{prefix}' does not exist."
            )

        sequence.current_number += 1

        self.db.commit()
        self.db.refresh(sequence)

        number = (
            f"{sequence.prefix}-"
            f"{sequence.current_number:0{sequence.digit_length}d}"
        )

        return number