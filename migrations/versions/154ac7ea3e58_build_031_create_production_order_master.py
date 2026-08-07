"""Build-031 Create Production Order Master

Revision ID: 154ac7ea3e58
Revises: 1460fac20de2
Create Date: 2026-08-07 12:20:55.059260

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.

revision: str = "154ac7ea3e58"

down_revision: Union[str, Sequence[str], None] = "1460fac20de2"

branch_labels: Union[str, Sequence[str], None] = None

depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create Production Order Master table."""

    op.create_table(
        "production_order_masters",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "production_order_no",
            sa.String(length=50),
            nullable=False,
        ),

        sa.Column(
            "production_order_date",
            sa.DateTime(timezone=True),
            nullable=False,
        ),

        sa.Column(
            "job_order_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "status",
            sa.String(length=50),
            nullable=False,
            server_default="Open",
        ),

        sa.Column(
            "priority",
            sa.String(length=30),
            nullable=False,
            server_default="Normal",
        ),

        sa.Column(
            "planned_start_date",
            sa.DateTime(timezone=True),
            nullable=True,
        ),

        sa.Column(
            "planned_end_date",
            sa.DateTime(timezone=True),
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

        # IMPORTANT:
        # Build-030 actual table name is job_order_master
        sa.ForeignKeyConstraint(
            ["job_order_id"],
            ["job_order_master.id"],
        ),

        sa.UniqueConstraint(
            "production_order_no",
        ),
    )

    op.create_index(
        op.f("ix_production_order_masters_id"),
        "production_order_masters",
        ["id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_production_order_masters_production_order_no"),
        "production_order_masters",
        ["production_order_no"],
        unique=True,
    )

    op.create_index(
        op.f("ix_production_order_masters_job_order_id"),
        "production_order_masters",
        ["job_order_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_production_order_masters_status"),
        "production_order_masters",
        ["status"],
        unique=False,
    )


def downgrade() -> None:
    """Drop Production Order Master table."""

    op.drop_index(
        op.f("ix_production_order_masters_status"),
        table_name="production_order_masters",
    )

    op.drop_index(
        op.f("ix_production_order_masters_job_order_id"),
        table_name="production_order_masters",
    )

    op.drop_index(
        op.f("ix_production_order_masters_production_order_no"),
        table_name="production_order_masters",
    )

    op.drop_index(
        op.f("ix_production_order_masters_id"),
        table_name="production_order_masters",
    )

    op.drop_table("production_order_masters")