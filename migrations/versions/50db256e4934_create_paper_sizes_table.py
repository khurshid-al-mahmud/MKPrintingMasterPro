"""Create paper_sizes table

Revision ID: 50db256e4934
Revises: 94e3402b6e12
Create Date: 2026-07-20

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "50db256e4934"
down_revision: Union[str, Sequence[str], None] = "94e3402b6e12"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "paper_sizes",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
        ),
        sa.Column(
            "paper_size_code",
            sa.String(length=30),
            nullable=False,
            unique=True,
        ),
        sa.Column(
            "paper_size_name",
            sa.String(length=150),
            nullable=False,
            unique=True,
        ),
        sa.Column(
            "width_mm",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "height_mm",
            sa.Integer(),
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
    )

    op.create_index(
        "ix_paper_sizes_id",
        "paper_sizes",
        ["id"],
    )

    op.create_index(
        "ix_paper_sizes_paper_size_code",
        "paper_sizes",
        ["paper_size_code"],
        unique=True,
    )

    op.create_index(
        "ix_paper_sizes_paper_size_name",
        "paper_sizes",
        ["paper_size_name"],
        unique=True,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        "ix_paper_sizes_paper_size_name",
        table_name="paper_sizes",
    )

    op.drop_index(
        "ix_paper_sizes_paper_size_code",
        table_name="paper_sizes",
    )

    op.drop_index(
        "ix_paper_sizes_id",
        table_name="paper_sizes",
    )

    op.drop_table("paper_sizes")