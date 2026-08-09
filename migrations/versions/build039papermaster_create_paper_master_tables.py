"""
Create Paper GSM and Paper Type Master tables.

Build-039 Pre-Entry Schema Preparation
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "build039papermaster"
down_revision: Union[str, None] = "build035status"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ==================================================
    # Paper GSM Master
    # ==================================================

    op.create_table(
        "paper_gsms",

        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "gsm_code",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "gsm_name",
            sa.String(length=100),
            nullable=False,
        ),

        sa.Column(
            "gsm_value",
            sa.Numeric(precision=8, scale=2),
            nullable=False,
        ),

        sa.Column(
            "paper_category",
            sa.String(length=100),
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
        "ix_paper_gsms_id",
        "paper_gsms",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_paper_gsms_gsm_code",
        "paper_gsms",
        ["gsm_code"],
        unique=True,
    )

    op.create_index(
        "ix_paper_gsms_gsm_name",
        "paper_gsms",
        ["gsm_name"],
        unique=True,
    )

    # ==================================================
    # Paper Type Master
    # ==================================================

    op.create_table(
        "paper_types",

        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "paper_type_code",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "paper_type_name",
            sa.String(length=100),
            nullable=False,
        ),

        sa.Column(
            "display_order",
            sa.Integer(),
            nullable=False,
            server_default="1",
        ),

        sa.Column(
            "remarks",
            sa.Text(),
            nullable=True,
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
        "ix_paper_types_id",
        "paper_types",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_paper_types_paper_type_code",
        "paper_types",
        ["paper_type_code"],
        unique=True,
    )

    op.create_index(
        "ix_paper_types_paper_type_name",
        "paper_types",
        ["paper_type_name"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_paper_types_paper_type_name",
        table_name="paper_types",
    )

    op.drop_index(
        "ix_paper_types_paper_type_code",
        table_name="paper_types",
    )

    op.drop_index(
        "ix_paper_types_id",
        table_name="paper_types",
    )

    op.drop_table("paper_types")

    op.drop_index(
        "ix_paper_gsms_gsm_name",
        table_name="paper_gsms",
    )

    op.drop_index(
        "ix_paper_gsms_gsm_code",
        table_name="paper_gsms",
    )

    op.drop_index(
        "ix_paper_gsms_id",
        table_name="paper_gsms",
    )

    op.drop_table("paper_gsms")
