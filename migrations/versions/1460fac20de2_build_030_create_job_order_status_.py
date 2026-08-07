"""Build-030 Create Job Order Status History

Revision ID: 1460fac20de2
Revises: 5648009222b6
Create Date: 2026-08-07 00:33:32.516848

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1460fac20de2'
down_revision: Union[str, Sequence[str], None] = '5648009222b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""

    # ===========================
    # Build-030 Phase-6 Step-3
    # Create Job Order Status History
    # ===========================

    op.create_table(
        'job_order_status_history',

        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            'job_order_id',
            sa.Integer(),
            nullable=False
        ),

        sa.Column(
            'old_status',
            sa.String(length=50),
            nullable=True
        ),

        sa.Column(
            'new_status',
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            'changed_by',
            sa.String(length=100),
            nullable=True
        ),

        sa.Column(
            'remarks',
            sa.String(length=255),
            nullable=True
        ),

        sa.Column(
            'changed_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=True
        ),

        sa.ForeignKeyConstraint(
            ['job_order_id'],
            ['job_order_master.id']
        ),

        sa.PrimaryKeyConstraint(
            'id'
        )
    )


    op.create_index(
        op.f('ix_job_order_status_history_id'),
        'job_order_status_history',
        ['id'],
        unique=False
    )



def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f('ix_job_order_status_history_id'),
        table_name='job_order_status_history'
    )

    op.drop_table(
        'job_order_status_history'
    )