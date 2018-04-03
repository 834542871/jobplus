"""empty message

Revision ID: 964383c7a3b5
Revises: 5f81ad8af0ed
Create Date: 2017-12-05 17:32:02.689485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '964383c7a3b5'
down_revision = '5f81ad8af0ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job', sa.Column('is_disable', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'is_disable')
    # ### end Alembic commands ###
