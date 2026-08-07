"""Build-030 Create Job Order Tables

Revision ID: 5648009222b6
Revises: 5fdd16910994
Create Date: 2026-08-06 23:27:17.947684
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5648009222b6"
down_revision: Union[str, Sequence[str], None] = "5fdd16910994"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "job_order_master",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "job_order_no",
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column(
            "job_order_date",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.Column(
            "invoice_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "quotation_id",
            sa.Integer(),
            nullable=True,
        ),
        sa.Column(
            "customer_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column(
            "priority",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "delivery_date",
            sa.Date(),
            nullable=True,
        ),
        sa.Column(
            "remarks",
            sa.String(length=1000),
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
            ["customer_id"],
            ["parties.id"],
        ),
        sa.ForeignKeyConstraint(
            ["invoice_id"],
            ["invoice_masters.id"],
        ),
        sa.ForeignKeyConstraint(
            ["quotation_id"],
            ["quotation_master.id"],
        ),
    )

    op.create_index(
        op.f("ix_job_order_master_customer_id"),
        "job_order_master",
        ["customer_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_job_order_master_id"),
        "job_order_master",
        ["id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_job_order_master_invoice_id"),
        "job_order_master",
        ["invoice_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_job_order_master_job_order_no"),
        "job_order_master",
        ["job_order_no"],
        unique=True,
    )

    op.create_index(
        op.f("ix_job_order_master_quotation_id"),
        "job_order_master",
        ["quotation_id"],
        unique=False,
    )

    op.create_table(
        "job_order_items",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "job_order_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "product_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "description",
            sa.String(length=1000),
            nullable=False,
        ),
        sa.Column(
            "quantity",
            sa.Float(),
            nullable=False,
        ),
        sa.Column(
            "unit",
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column(
            "specification",
            sa.String(length=2000),
            nullable=True,
        ),
        sa.Column(
            "remarks",
            sa.String(length=1000),
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
            ["job_order_id"],
            ["job_order_master.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
    )

    op.create_index(
        op.f("ix_job_order_items_id"),
        "job_order_items",
        ["id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_job_order_items_job_order_id"),
        "job_order_items",
        ["job_order_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_job_order_items_product_id"),
        "job_order_items",
        ["product_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_job_order_items_product_id"),
        table_name="job_order_items",
    )

    op.drop_index(
        op.f("ix_job_order_items_job_order_id"),
        table_name="job_order_items",
    )

    op.drop_index(
        op.f("ix_job_order_items_id"),
        table_name="job_order_items",
    )

    op.drop_table("job_order_items")

    op.drop_index(
        op.f("ix_job_order_master_quotation_id"),
        table_name="job_order_master",
    )

    op.drop_index(
        op.f("ix_job_order_master_job_order_no"),
        table_name="job_order_master",
    )

    op.drop_index(
        op.f("ix_job_order_master_invoice_id"),
        table_name="job_order_master",
    )

    op.drop_index(
        op.f("ix_job_order_master_id"),
        table_name="job_order_master",
    )

    op.drop_index(
        op.f("ix_job_order_master_customer_id"),
        table_name="job_order_master",
    )

    op.drop_table("job_order_master")