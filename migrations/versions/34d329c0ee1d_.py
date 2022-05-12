"""empty message

Revision ID: 34d329c0ee1d
Revises: f4cb5d85c757
Create Date: 2022-05-12 21:40:01.865962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34d329c0ee1d'
down_revision = 'f4cb5d85c757'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitchs', sa.Column('pitchAuthor', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitchs', 'pitchAuthor')
    # ### end Alembic commands ###