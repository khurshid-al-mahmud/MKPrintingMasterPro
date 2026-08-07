"""
Build-031 Create Operation Assignment

Revision ID: 368c12980e5f
Revises: c652bc738552
Create Date: 2026-08-07 17:02:32.878010

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "368c12980e5f"
down_revision: Union[str, Sequence[str], None] = "c652bc738552"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade schema."""

    # ===========================
    # Operation Assignment Table
    # Build-031
    # ===========================

    op.create_table(
        "operation_assignments",

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
            "operation_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "sequence_no",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "assigned_party_id",
            sa.Integer(),
            nullable=True,
        ),

        sa.Column(
            "assigned_type",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "status",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "is_required",
            sa.Boolean(),
            nullable=False,
        ),

        sa.Column(
            "is_completed",
            sa.Boolean(),
            nullable=False,
        ),

        sa.Column(
            "planned_start_date",
            sa.Date(),
            nullable=True,
        ),

        sa.Column(
            "planned_end_date",
            sa.Date(),
            nullable=True,
        ),

        sa.Column(
            "instructions",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "remarks",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "created_by",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "updated_by",
            sa.String(length=100),
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
            ["operation_id"],
            ["operation_masters.id"],
            ondelete="RESTRICT",
        ),

        sa.ForeignKeyConstraint(
            ["assigned_party_id"],
            ["parties.id"],
            ondelete="SET NULL",
        ),

        sa.PrimaryKeyConstraint(
            "id"
        ),
    )


    # ===========================
    # Indexes
    # ===========================

    op.create_index(
        "ix_operation_assignments_id",
        "operation_assignments",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_operation_assignments_production_order_id",
        "operation_assignments",
        ["production_order_id"],
        unique=False,
    )

    op.create_index(
        "ix_operation_assignments_operation_id",
        "operation_assignments",
        ["operation_id"],
        unique=False,
    )

    op.create_index(
        "ix_operation_assignments_sequence_no",
        "operation_assignments",
        ["sequence_no"],
        unique=False,
    )

    op.create_index(
        "ix_operation_assignments_assigned_party_id",
        "operation_assignments",
        ["assigned_party_id"],
        unique=False,
    )

    op.create_index(
        "ix_operation_assignments_assigned_type",
        "operation_assignments",
        ["assigned_type"],
        unique=False,
    )

    op.create_index(
        "ix_operation_assignments_status",
        "operation_assignments",
        ["status"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        "ix_operation_assignments_status",
        table_name="operation_assignments",
    )

    op.drop_index(
        "ix_operation_assignments_assigned_type",
        table_name="operation_assignments",
    )

    op.drop_index(
        "ix_operation_assignments_assigned_party_id",
        table_name="operation_assignments",
    )

    op.drop_index(
        "ix_operation_assignments_sequence_no",
        table_name="operation_assignments",
    )

    op.drop_index(
        "ix_operation_assignments_operation_id",
        table_name="operation_assignments",
    )

    op.drop_index(
        "ix_operation_assignments_production_order_id",
        table_name="operation_assignments",
    )

    op.drop_index(
        "ix_operation_assignments_id",
        table_name="operation_assignments",
    )

    op.drop_table(
        "operation_assignments"
    )