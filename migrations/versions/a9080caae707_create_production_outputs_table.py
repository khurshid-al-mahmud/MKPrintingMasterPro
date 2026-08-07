"""
create production outputs table

Revision ID: a9080caae707
Revises: c5739bf02913
Create Date: 2026-08-07

Build-034
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.

revision: str = "a9080caae707"
down_revision: Union[str, None] = "c5739bf02913"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Create production_outputs table.
    """

    op.create_table(
        "production_outputs",

        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),

        sa.Column(
            "production_operation_execution_id",
            sa.Integer(),
            nullable=False,
        ),

        sa.Column(
            "output_quantity",
            sa.Numeric(
                precision=18,
                scale=3,
            ),
            nullable=False,
        ),

        sa.Column(
            "reject_quantity",
            sa.Numeric(
                precision=18,
                scale=3,
            ),
            nullable=True,
        ),

        sa.Column(
            "output_status",
            sa.String(
                length=30
            ),
            nullable=False,
        ),

        sa.Column(
            "operator_name",
            sa.String(
                length=100
            ),
            nullable=True,
        ),

        sa.Column(
            "remarks",
            sa.Text(),
            nullable=True,
        ),

        sa.Column(
            "created_at",
            sa.DateTime(
                timezone=True
            ),
            nullable=False,
        ),

        sa.ForeignKeyConstraint(
            [
                "production_operation_execution_id"
            ],
            [
                "production_operation_executions.id"
            ],
            ondelete="CASCADE",
        ),

        sa.PrimaryKeyConstraint(
            "id"
        ),
    )


def downgrade() -> None:
    """
    Drop production_outputs table.
    """

    op.drop_table(
        "production_outputs"
    )