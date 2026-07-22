"""Build-010: Create System Setting Master

Revision ID: 01a57eab17a1
Revises: fa3844a8da3f
Create Date: 2026-07-21

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "01a57eab17a1"
down_revision: Union[str, Sequence[str], None] = "fa3844a8da3f"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "system_settings",

        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
        ),

        sa.Column(
            "setting_key",
            sa.String(length=100),
            nullable=False,
            unique=True,
        ),

        sa.Column(
            "setting_value",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "description",
            sa.String(length=255),
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
        "ix_system_settings_id",
        "system_settings",
        ["id"],
    )

    op.create_index(
        "ix_system_settings_setting_key",
        "system_settings",
        ["setting_key"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index(
        "ix_system_settings_setting_key",
        table_name="system_settings",
    )

    op.drop_index(
        "ix_system_settings_id",
        table_name="system_settings",
    )

    op.drop_table("system_settings")