"""Build-011: Company Profile Master

Revision ID: 6d8e58c64e9e
Revises: 01a57eab17a1
Create Date: 2026-07-22

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers
revision: str = "6d8e58c64e9e"
down_revision: Union[str, Sequence[str], None] = "01a57eab17a1"
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        "company_profiles",

        sa.Column("id", sa.Integer(), primary_key=True),

        sa.Column(
            "company_name",
            sa.String(length=200),
            nullable=False,
        ),

        sa.Column(
            "company_name_en",
            sa.String(length=200),
            nullable=True,
        ),

        sa.Column(
            "logo_path",
            sa.String(length=500),
            nullable=True,
        ),

        sa.Column(
            "address",
            sa.String(length=500),
            nullable=True,
        ),

        sa.Column(
            "mobile",
            sa.String(length=50),
            nullable=True,
        ),

        sa.Column(
            "phone",
            sa.String(length=50),
            nullable=True,
        ),

        sa.Column(
            "email",
            sa.String(length=200),
            nullable=True,
        ),

        sa.Column(
            "website",
            sa.String(length=300),
            nullable=True,
        ),

        sa.Column(
            "facebook",
            sa.String(length=300),
            nullable=True,
        ),

        # Confidential Information

        sa.Column(
            "trade_license",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "bin_number",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "tin_number",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "vat_number",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "bank_name",
            sa.String(length=200),
            nullable=True,
        ),

        sa.Column(
            "bank_account_name",
            sa.String(length=200),
            nullable=True,
        ),

        sa.Column(
            "bank_account_number",
            sa.String(length=100),
            nullable=True,
        ),

        sa.Column(
            "bank_branch",
            sa.String(length=200),
            nullable=True,
        ),

        sa.Column(
            "confidential_visible",
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


def downgrade() -> None:

    op.drop_table("company_profiles")