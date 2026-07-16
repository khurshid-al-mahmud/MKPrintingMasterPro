"""
Seed default number sequences.

Run this once after installing the ERP database.
"""

from sqlalchemy.orm import Session

from app.models.number_sequence import NumberSequence


def seed_number_sequences(db: Session) -> None:
    """Insert default number sequences if they do not exist."""

    sequences = [
        ("CUS", "Customer"),
        ("SUP", "Supplier"),
        ("EMP", "Employee"),
        ("QUO", "Quotation"),
        ("JOB", "Job Order"),
        ("INV", "Invoice"),
        ("PUR", "Purchase"),
        ("PAY", "Payment"),
    ]

    for prefix, description in sequences:
        exists = (
            db.query(NumberSequence)
            .filter(NumberSequence.prefix == prefix)
            .first()
        )

        if exists is None:
            db.add(
                NumberSequence(
                    prefix=prefix,
                    description=description,
                    current_number=0,
                    digit_length=6,
                )
            )

    db.commit()