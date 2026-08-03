"""create_product_template_master

Revision ID: 928b98c1f181
Revises: a07319cd3b35
Create Date: 2026-08-03 18:33:56.680318

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "928b98c1f181"
down_revision: Union[str, Sequence[str], None] = "a07319cd3b35"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "product_templates",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
        ),

        sa.Column(
            "template_code",
            sa.String(30),
            nullable=False,
        ),

        sa.Column(
            "template_name",
            sa.String(150),
            nullable=False,
        ),

        sa.Column(
            "product_id",
            sa.Integer(),
            sa.ForeignKey("products.id"),
            nullable=False,
        ),

        sa.Column(
            "description",
            sa.String(300),
            nullable=True,
        ),

        sa.Column(
            "is_default",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("false"),
        ),

        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    op.create_index(
        "ix_product_templates_id",
        "product_templates",
        ["id"],
    )

    op.create_index(
        "ix_product_templates_template_code",
        "product_templates",
        ["template_code"],
        unique=True,
    )

    op.create_index(
        "ix_product_templates_template_name",
        "product_templates",
        ["template_name"],
    )

    op.create_index(
        "ix_product_templates_product_id",
        "product_templates",
        ["product_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        "ix_product_templates_product_id",
        table_name="product_templates",
    )

    op.drop_index(
        "ix_product_templates_template_name",
        table_name="product_templates",
    )

    op.drop_index(
        "ix_product_templates_template_code",
        table_name="product_templates",
    )

    op.drop_index(
        "ix_product_templates_id",
        table_name="product_templates",
    )

    op.drop_table("product_templates")