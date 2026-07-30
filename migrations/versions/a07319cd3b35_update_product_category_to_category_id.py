"""update_product_category_to_category_id

Revision ID: a07319cd3b35
Revises: c4171da6af41
Create Date: 2026-07-30

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "a07319cd3b35"
down_revision: Union[str, None] = "c4171da6af41"
branch_labels = None
depends_on = None


def upgrade() -> None:

    # Remove old column
    op.drop_column(
        "products",
        "product_category",
    )

    # Add new FK column
    op.add_column(
        "products",
        sa.Column(
            "category_id",
            sa.Integer(),
            nullable=True,
        ),
    )

    # Foreign Key
    op.create_foreign_key(
        "fk_products_category_id",
        "products",
        "product_categories",
        ["category_id"],
        ["id"],
    )

    # Index
    op.create_index(
        "ix_products_category_id",
        "products",
        ["category_id"],
        unique=False,
    )


def downgrade() -> None:

    op.drop_index(
        "ix_products_category_id",
        table_name="products",
    )

    op.drop_constraint(
        "fk_products_category_id",
        "products",
        type_="foreignkey",
    )

    op.drop_column(
        "products",
        "category_id",
    )

    op.add_column(
        "products",
        sa.Column(
            "product_category",
            sa.String(100),
            nullable=False,
        ),
    )