"""create the owners table

Revision ID: cc048a2a464c
Revises: 899f4f2c3a3f
Create Date: 2020-12-25 15:24:35.615791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc048a2a464c'
down_revision = '899f4f2c3a3f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "owners",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.String(50), nullable=False),
        sa.Column("last_name", sa.String(50), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table('owners')
