"""
Build-031 Create Operation Master

Revision ID: c652bc738552
Revises: 154ac7ea3e58
Create Date: 2026-08-07 16:17:34.709352

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# ============================================================
# Revision identifiers, used by Alembic.
# ============================================================

revision: str = "c652bc738552"

down_revision: Union[str, Sequence[str], None] = "154ac7ea3e58"

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None


# ============================================================
# Upgrade
# ============================================================

def upgrade() -> None:
    """
    Create Operation Master table.

    Build-031

    This migration intentionally contains ONLY the
    Operation Master changes.

    Unrelated schema differences detected by Alembic
    autogenerate are NOT included here.
    """

    # ========================================================
    # Operation Master
    # ========================================================

    op.create_table(
        "operation_masters",

        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "operation_code",
            sa.String(length=50),
            nullable=False,
        ),

        sa.Column(
            "operation_name",
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
        ),

        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
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

        sa.PrimaryKeyConstraint("id"),
    )

    # ========================================================
    # Operation Master Indexes
    # ========================================================

    op.create_index(
        op.f("ix_operation_masters_id"),
        "operation_masters",
        ["id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_operation_masters_operation_code"),
        "operation_masters",
        ["operation_code"],
        unique=True,
    )

    op.create_index(
        op.f("ix_operation_masters_operation_name"),
        "operation_masters",
        ["operation_name"],
        unique=True,
    )

    op.create_index(
        op.f("ix_operation_masters_is_active"),
        "operation_masters",
        ["is_active"],
        unique=False,
    )


# ============================================================
# Downgrade
# ============================================================

def downgrade() -> None:
    """
    Remove Operation Master table.

    Build-031
    """

    # ========================================================
    # Drop Operation Master Indexes
    # ========================================================

    op.drop_index(
        op.f("ix_operation_masters_is_active"),
        table_name="operation_masters",
    )

    op.drop_index(
        op.f("ix_operation_masters_operation_name"),
        table_name="operation_masters",
    )

    op.drop_index(
        op.f("ix_operation_masters_operation_code"),
        table_name="operation_masters",
    )

    op.drop_index(
        op.f("ix_operation_masters_id"),
        table_name="operation_masters",
    )

    # ========================================================
    # Drop Operation Master Table
    # ========================================================

    op.drop_table("operation_masters")