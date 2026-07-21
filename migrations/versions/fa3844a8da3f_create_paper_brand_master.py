"""Create Paper Brand Master

Revision ID: fa3844a8da3f
Revises: 05b1356f245d
Create Date: 2026-07-21

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "fa3844a8da3f"
down_revision: Union[str, Sequence[str], None] = "05b1356f245d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create paper_brands table."""

    op.create_table(
        "paper_brands",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
        ),

        sa.Column(
            "paper_brand_code",
            sa.String(length=30),
            nullable=False,
        ),

        sa.Column(
            "paper_brand_name",
            sa.String(length=150),
            nullable=False,
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
            server_default=sa.text("true"),
        ),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )

    op.create_index(
        "ix_paper_brands_id",
        "paper_brands",
        ["id"],
    )

    op.create_index(
        "ix_paper_brands_paper_brand_code",
        "paper_brands",
        ["paper_brand_code"],
        unique=True,
    )

    op.create_index(
        "ix_paper_brands_paper_brand_name",
        "paper_brands",
        ["paper_brand_name"],
        unique=True,
    )


def downgrade() -> None:
    """Drop paper_brands table."""

    op.drop_index(
        "ix_paper_brands_paper_brand_name",
        table_name="paper_brands",
    )

    op.drop_index(
        "ix_paper_brands_paper_brand_code",
        table_name="paper_brands",
    )

    op.drop_index(
        "ix_paper_brands_id",
        table_name="paper_brands",
    )

    op.drop_table("paper_brands")