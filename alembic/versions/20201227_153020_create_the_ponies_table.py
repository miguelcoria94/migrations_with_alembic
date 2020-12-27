"""create the ponies table

Revision ID: 6c1203eb5599
Revises: cc048a2a464c
Create Date: 2020-12-27 15:30:20.360771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c1203eb5599'
down_revision = 'cc048a2a464c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ponies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("breed", sa.String(20), nullable=False),
        sa.Column("birth_year", sa.Integer, nullable=False),
        sa.Column("owner_id",
                  sa.Integer,
                  sa.ForeignKey("owners.id"),
                  nullable=False)
    )


def downgrade():
    op.drop_table("ponies")


def downgrade():
    pass
