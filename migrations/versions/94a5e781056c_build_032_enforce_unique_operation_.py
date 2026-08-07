"""
MKPrintingMasterPro ERP

Build-032
Enforce unique operation assignment sequence.

Prevents duplicate operation assignments for the
same production order, operation, and sequence number.
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "94a5e781056c"
down_revision: Union[str, Sequence[str], None] = "368c12980e5f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


CONSTRAINT_NAME = "uq_operation_assignment_order_operation_sequence"


def upgrade() -> None:
    """
    Add database-level uniqueness protection for
    production order + operation + sequence.
    """

    op.create_unique_constraint(
        CONSTRAINT_NAME,
        "operation_assignments",
        [
            "production_order_id",
            "operation_id",
            "sequence_no",
        ],
    )


def downgrade() -> None:
    """
    Remove the unique constraint.
    """

    op.drop_constraint(
        CONSTRAINT_NAME,
        "operation_assignments",
        type_="unique",
    )