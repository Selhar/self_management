"""add cards table

Revision ID: 2019a64025a0
Revises: f081d8542cc8
Create Date: 2021-07-03 04:04:07.137008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2019a64025a0'
down_revision = 'f081d8542cc8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cards',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text', sa.String(250), nullable=False),
        sa.Column('position', sa.Integer, nullable=False, unique=True),
        sa.Column('column_id', sa.Integer, sa.ForeignKey("columns.id"), nullable=False, unique=True),
    )

def downgrade():
    op.drop_table('cards')
