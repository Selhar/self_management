"""add columns table

Revision ID: f081d8542cc8
Revises: 
Create Date: 2021-07-03 03:56:17.181935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f081d8542cc8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'columns',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(250), nullable=False),
        sa.Column('position', sa.Integer, nullable=False, unique=True),
    )

def downgrade():
    op.drop_table('columns')
