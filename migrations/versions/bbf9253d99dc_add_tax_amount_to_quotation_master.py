"""Add tax_amount to quotation_master

Revision ID: bbf9253d99dc
Revises: 6d2deb872115
Create Date: 2026-08-05 19:24:28.372319

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bbf9253d99dc"
down_revision: Union[str, Sequence[str], None] = "6d2deb872115"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Upgrade schema.
    """

    op.add_column(
        "quotation_master",
        sa.Column(
            "tax_amount",
            sa.Numeric(
                precision=18,
                scale=2,
            ),
            nullable=True,
        ),
    )


def downgrade() -> None:
    """
    Downgrade schema.
    """

    op.drop_column(
        "quotation_master",
        "tax_amount",
    )