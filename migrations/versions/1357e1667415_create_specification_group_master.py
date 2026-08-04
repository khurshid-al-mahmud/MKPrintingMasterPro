"""Create Specification Group Master

Revision ID: 1357e1667415
Revises: 928b98c1f181
Create Date: 2026-08-04 00:32:21.422275
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1357e1667415"
down_revision: Union[str, Sequence[str], None] = "928b98c1f181"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "specification_groups",
        sa.Column(
            "id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
        ),
        sa.Column(
            "group_code",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "group_name",
            sa.String(length=150),
            nullable=False,
        ),
        sa.Column(
            "template_id",
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
            "description",
            sa.String(length=300),
            nullable=True,
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
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["template_id"],
            ["product_templates.id"],
        ),
    )

    op.create_index(
        "ix_specification_groups_id",
        "specification_groups",
        ["id"],
    )

    op.create_index(
        "ix_specification_groups_group_code",
        "specification_groups",
        ["group_code"],
        unique=True,
    )

    op.create_index(
        "ix_specification_groups_group_name",
        "specification_groups",
        ["group_name"],
    )

    op.create_index(
        "ix_specification_groups_template_id",
        "specification_groups",
        ["template_id"],
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        "ix_specification_groups_template_id",
        table_name="specification_groups",
    )

    op.drop_index(
        "ix_specification_groups_group_name",
        table_name="specification_groups",
    )

    op.drop_index(
        "ix_specification_groups_group_code",
        table_name="specification_groups",
    )

    op.drop_index(
        "ix_specification_groups_id",
        table_name="specification_groups",
    )

    op.drop_table(
        "specification_groups",
    )