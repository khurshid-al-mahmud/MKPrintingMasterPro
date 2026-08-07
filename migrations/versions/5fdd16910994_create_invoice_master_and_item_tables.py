"""Create invoice master and item tables

Revision ID: 5fdd16910994
Revises: bbf9253d99dc
Create Date: 2026-08-05 22:45:09.069992
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5fdd16910994"
down_revision: Union[str, Sequence[str], None] = "bbf9253d99dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "invoice_masters",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("invoice_no", sa.String(length=50), nullable=False),
        sa.Column("invoice_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("customer_id", sa.Integer(), nullable=False),
        sa.Column("quotation_id", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("remarks", sa.String(length=500), nullable=True),
        sa.Column("subtotal", sa.Float(), nullable=False),
        sa.Column("discount_amount", sa.Float(), nullable=False),
        sa.Column("vat_amount", sa.Float(), nullable=False),
        sa.Column("tax_amount", sa.Float(), nullable=False),
        sa.Column("grand_total", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["customer_id"], ["parties.id"]),
        sa.ForeignKeyConstraint(["quotation_id"], ["quotation_master.id"]),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_invoice_masters_customer_id",
        "invoice_masters",
        ["customer_id"],
        unique=False,
    )

    op.create_index(
        "ix_invoice_masters_id",
        "invoice_masters",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_invoice_masters_invoice_no",
        "invoice_masters",
        ["invoice_no"],
        unique=True,
    )

    op.create_table(
        "invoice_items",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("invoice_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(length=1000), nullable=False),
        sa.Column("quantity", sa.Float(), nullable=False),
        sa.Column("unit", sa.String(length=50), nullable=False),
        sa.Column("unit_price", sa.Float(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("specification", sa.String(length=2000), nullable=True),
        sa.Column("remarks", sa.String(length=1000), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["invoice_id"],
            ["invoice_masters.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_invoice_items_id",
        "invoice_items",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_invoice_items_invoice_id",
        "invoice_items",
        ["invoice_id"],
        unique=False,
    )

    op.create_index(
        "ix_invoice_items_product_id",
        "invoice_items",
        ["product_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        "ix_invoice_items_product_id",
        table_name="invoice_items",
    )

    op.drop_index(
        "ix_invoice_items_invoice_id",
        table_name="invoice_items",
    )

    op.drop_index(
        "ix_invoice_items_id",
        table_name="invoice_items",
    )

    op.drop_table("invoice_items")

    op.drop_index(
        "ix_invoice_masters_invoice_no",
        table_name="invoice_masters",
    )

    op.drop_index(
        "ix_invoice_masters_id",
        table_name="invoice_masters",
    )

    op.drop_index(
        "ix_invoice_masters_customer_id",
        table_name="invoice_masters",
    )

    op.drop_table("invoice_masters")