"""
Build-033 Create Production Operation Execution

Revision ID: c5739bf02913
Revises: 94a5e781056c
Create Date: 2026-08-07
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c5739bf02913"
down_revision: Union[str, Sequence[str], None] = "94a5e781056c"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "production_operation_executions",

        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "production_order_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "operation_assignment_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "status",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "planned_quantity",
            sa.Numeric(precision=18, scale=3),
            nullable=True,
        ),

        sa.Column(
            "completed_quantity",
            sa.Numeric(precision=18, scale=3),
            nullable=True,
        ),

        sa.Column(
            "reject_quantity",
            sa.Numeric(precision=18, scale=3),
            nullable=True,
        ),

        sa.Column(
            "actual_start_time",
            sa.DateTime(timezone=True),
            nullable=True,
        ),

        sa.Column(
            "actual_end_time",
            sa.DateTime(timezone=True),
            nullable=True,
        ),

        sa.Column(
            "operator_name",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "remarks",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),

        sa.ForeignKeyConstraint(
            ["production_order_id"],
            ["production_order_masters.id"],
            ondelete="CASCADE",
        ),

        sa.ForeignKeyConstraint(
            ["operation_assignment_id"],
            ["operation_assignments.id"],
            ondelete="CASCADE",
        ),

        sa.PrimaryKeyConstraint("id"),
    )


    op.create_index(
        "ix_production_operation_executions_id",
        "production_operation_executions",
        ["id"],
    )


    op.create_index(
        "ix_production_operation_executions_production_order_id",
        "production_operation_executions",
        ["production_order_id"],
    )


    op.create_index(
        "ix_production_operation_executions_operation_assignment_id",
        "production_operation_executions",
        ["operation_assignment_id"],
    )


    op.create_index(
        "ix_production_operation_executions_status",
        "production_operation_executions",
        ["status"],
    )



def downgrade() -> None:

    op.drop_index(
        "ix_production_operation_executions_status",
        table_name="production_operation_executions",
    )

    op.drop_index(
        "ix_production_operation_executions_operation_assignment_id",
        table_name="production_operation_executions",
    )

    op.drop_index(
        "ix_production_operation_executions_production_order_id",
        table_name="production_operation_executions",
    )

    op.drop_index(
        "ix_production_operation_executions_id",
        table_name="production_operation_executions",
    )

    op.drop_table(
        "production_operation_executions"
    )