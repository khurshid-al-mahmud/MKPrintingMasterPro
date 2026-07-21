"""Create binding_types table

Revision ID: 05b1356f245d
Revises: 50db256e4934
Create Date: 2026-07-21

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers
revision: str = "05b1356f245d"
down_revision: Union[str, Sequence[str], None] = "50db256e4934"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create binding_types table."""

    op.create_table(
        "binding_types",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column(
            "binding_type_code",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "binding_type_name",
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
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )

    op.create_index(
        "ix_binding_types_id",
        "binding_types",
        ["id"],
        unique=False,
    )

    op.create_index(
        "ix_binding_types_binding_type_code",
        "binding_types",
        ["binding_type_code"],
        unique=True,
    )

    op.create_index(
        "ix_binding_types_binding_type_name",
        "binding_types",
        ["binding_type_name"],
        unique=True,
    )


def downgrade() -> None:
    """Drop binding_types table."""

    op.drop_index(
        "ix_binding_types_binding_type_name",
        table_name="binding_types",
    )

    op.drop_index(
        "ix_binding_types_binding_type_code",
        table_name="binding_types",
    )

    op.drop_index(
        "ix_binding_types_id",
        table_name="binding_types",
    )

    op.drop_table("binding_types")