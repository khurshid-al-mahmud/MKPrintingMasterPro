"""
Build-040 Add Machine Linkage to Production Operations

Revision ID: build040machinelink
Revises: build039papermaster
Create Date: 2026-08-10

Adds machine linkage to:

- operation_assignments
- production_operation_executions

Machine linkage is nullable so existing production records remain valid.
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "build040machinelink"

down_revision: Union[str, Sequence[str], None] = "build039papermaster"

branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Add machine linkage to production operation tracking.
    """

    # ========================================================
    # Operation Assignment
    # ========================================================

    op.add_column(
        "operation_assignments",
        sa.Column(
            "machine_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.create_index(
        "ix_operation_assignments_machine_id",
        "operation_assignments",
        ["machine_id"],
        unique=False,
    )

    op.create_foreign_key(
        "fk_operation_assignments_machine_id",
        "operation_assignments",
        "machines",
        ["machine_id"],
        ["id"],
        ondelete="SET NULL",
    )

    # ========================================================
    # Production Operation Execution
    # ========================================================

    op.add_column(
        "production_operation_executions",
        sa.Column(
            "machine_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    op.create_index(
        "ix_production_operation_executions_machine_id",
        "production_operation_executions",
        ["machine_id"],
        unique=False,
    )

    op.create_foreign_key(
        "fk_production_operation_executions_machine_id",
        "production_operation_executions",
        "machines",
        ["machine_id"],
        ["id"],
        ondelete="SET NULL",
    )


def downgrade() -> None:
    """
    Remove machine linkage from production operation tracking.
    """

    op.drop_constraint(
        "fk_production_operation_executions_machine_id",
        "production_operation_executions",
        type_="foreignkey",
    )

    op.drop_index(
        "ix_production_operation_executions_machine_id",
        table_name="production_operation_executions",
    )

    op.drop_column(
        "production_operation_executions",
        "machine_id",
    )

    op.drop_constraint(
        "fk_operation_assignments_machine_id",
        "operation_assignments",
        type_="foreignkey",
    )

    op.drop_index(
        "ix_operation_assignments_machine_id",
        table_name="operation_assignments",
    )

    op.drop_column(
        "operation_assignments",
        "machine_id",
    )
