"""
Build-035

Production Operation Execution Status Master
Production Operation Execution History
Production Operation Execution Status History
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "build035status"
down_revision: Union[str, None] = "a9080caae707"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # ==================================================
    # Status Master
    # ==================================================

    op.create_table(
        "production_operation_execution_statuses",

        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "status_code",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "status_name",
            sa.String(length=100),
            nullable=False,
        ),

        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "display_order",
            sa.Integer(),
            nullable=False,
            server_default="1",
        ),

        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.true(),
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),

        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_production_operation_execution_statuses_id",
        "production_operation_execution_statuses",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_production_operation_execution_statuses_status_code",
        "production_operation_execution_statuses",
        ["status_code"],
        unique=True,
    )

    op.create_index(
        "ix_production_operation_execution_statuses_is_active",
        "production_operation_execution_statuses",
        ["is_active"],
        unique=False,
    )

    # ==================================================
    # Execution History
    # ==================================================

    op.create_table(
        "production_operation_execution_histories",

        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "production_operation_execution_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "previous_status",
            sa.String(length=30),
            nullable=True,
        ),

        sa.Column(
            "new_status",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "completed_quantity",
            sa.Numeric(
                precision=18,
                scale=3,
            ),
            nullable=True,
        ),

        sa.Column(
            "reject_quantity",
            sa.Numeric(
                precision=18,
                scale=3,
            ),
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
            server_default=sa.func.now(),
        ),

        sa.ForeignKeyConstraint(
            ["production_operation_execution_id"],
            ["production_operation_executions.id"],
            ondelete="CASCADE",
        ),

        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_production_operation_execution_histories_id",
        "production_operation_execution_histories",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_production_operation_execution_histories_execution_id",
        "production_operation_execution_histories",
        ["production_operation_execution_id"],
        unique=False,
    )

    # ==================================================
    # Status History
    # ==================================================

    op.create_table(
        "production_operation_execution_status_histories",

        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "production_operation_execution_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "previous_status",
            sa.String(length=30),
            nullable=True,
        ),

        sa.Column(
            "new_status",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "completed_quantity",
            sa.Numeric(
                precision=18,
                scale=3,
            ),
            nullable=True,
        ),

        sa.Column(
            "reject_quantity",
            sa.Numeric(
                precision=18,
                scale=3,
            ),
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
            server_default=sa.func.now(),
        ),

        sa.ForeignKeyConstraint(
            ["production_operation_execution_id"],
            ["production_operation_executions.id"],
            ondelete="CASCADE",
        ),

        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_production_operation_execution_status_histories_id",
        "production_operation_execution_status_histories",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_production_operation_execution_status_histories_execution_id",
        "production_operation_execution_status_histories",
        ["production_operation_execution_id"],
        unique=False,
    )

    # ==================================================
    # Default Statuses
    # ==================================================

    status_table = sa.table(
        "production_operation_execution_statuses",

        sa.column(
            "status_code",
            sa.String(length=30),
        ),

        sa.column(
            "status_name",
            sa.String(length=100),
        ),

        sa.column(
            "description",
            sa.Text(),
        ),

        sa.column(
            "display_order",
            sa.Integer(),
        ),

        sa.column(
            "is_active",
            sa.Boolean(),
        ),
    )

    op.bulk_insert(
        status_table,
        [
            {
                "status_code": "PENDING",
                "status_name": "Pending",
                "description": "Execution has not started.",
                "display_order": 1,
                "is_active": True,
            },
            {
                "status_code": "STARTED",
                "status_name": "Started",
                "description": "Production operation execution has started.",
                "display_order": 2,
                "is_active": True,
            },
            {
                "status_code": "COMPLETED",
                "status_name": "Completed",
                "description": "Production operation execution has completed.",
                "display_order": 3,
                "is_active": True,
            },
            {
                "status_code": "CANCELLED",
                "status_name": "Cancelled",
                "description": "Production operation execution was cancelled.",
                "display_order": 4,
                "is_active": True,
            },
        ],
    )


def downgrade() -> None:

    op.drop_index(
        "ix_production_operation_execution_status_histories_execution_id",
        table_name="production_operation_execution_status_histories",
    )

    op.drop_index(
        "ix_production_operation_execution_status_histories_id",
        table_name="production_operation_execution_status_histories",
    )

    op.drop_table(
        "production_operation_execution_status_histories",
    )

    op.drop_index(
        "ix_production_operation_execution_histories_execution_id",
        table_name="production_operation_execution_histories",
    )

    op.drop_index(
        "ix_production_operation_execution_histories_id",
        table_name="production_operation_execution_histories",
    )

    op.drop_table(
        "production_operation_execution_histories",
    )

    op.drop_index(
        "ix_production_operation_execution_statuses_is_active",
        table_name="production_operation_execution_statuses",
    )

    op.drop_index(
        "ix_production_operation_execution_statuses_status_code",
        table_name="production_operation_execution_statuses",
    )

    op.drop_index(
        "ix_production_operation_execution_statuses_id",
        table_name="production_operation_execution_statuses",
    )

    op.drop_table(
        "production_operation_execution_statuses",
    )
