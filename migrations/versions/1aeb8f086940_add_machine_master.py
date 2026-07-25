"""add_machine_master

Revision ID: 1aeb8f086940
Revises: 6d8e58c64e9e
Create Date: 2026-07-25

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "1aeb8f086940"
down_revision: Union[str, None] = "6d8e58c64e9e"
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "machines",

        sa.Column("id", sa.Integer(), primary_key=True),

        sa.Column("machine_code", sa.String(30), nullable=False),

        sa.Column("machine_name", sa.String(150), nullable=False),

        sa.Column("machine_type", sa.String(50), nullable=False),

        sa.Column("manufacturer", sa.String(100)),

        sa.Column("model", sa.String(100)),

        sa.Column("serial_number", sa.String(100)),

        sa.Column("asset_number", sa.String(100)),

        sa.Column("machine_location", sa.String(150)),

        sa.Column("operator_name", sa.String(100)),

        sa.Column("max_paper_width", sa.Numeric(10,2)),

        sa.Column("max_paper_height", sa.Numeric(10,2)),

        sa.Column("minimum_gsm", sa.Integer()),

        sa.Column("maximum_gsm", sa.Integer()),

        sa.Column("color_capacity", sa.Integer()),

        sa.Column("printing_speed", sa.Integer()),

        sa.Column("hourly_running_cost", sa.Numeric(12,2), nullable=False, server_default="0"),

        sa.Column("electric_consumption_kw", sa.Numeric(10,2)),

        sa.Column("purchase_date", sa.Date()),

        sa.Column("installation_date", sa.Date()),

        sa.Column("last_maintenance_date", sa.Date()),

        sa.Column("next_maintenance_date", sa.Date()),

        sa.Column("status", sa.String(30), nullable=False, server_default="Running"),

        sa.Column("remarks", sa.Text()),

        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),

        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),

        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    op.create_index("ix_machines_machine_code", "machines", ["machine_code"], unique=True)
    op.create_index("ix_machines_machine_name", "machines", ["machine_name"], unique=False)


def downgrade():

    op.drop_index("ix_machines_machine_name", table_name="machines")
    op.drop_index("ix_machines_machine_code", table_name="machines")
    op.drop_table("machines")