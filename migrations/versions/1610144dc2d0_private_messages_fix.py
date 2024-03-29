"""private messages - fix

Revision ID: 1610144dc2d0
Revises: c679e8f8b2d9
Create Date: 2021-04-29 19:38:13.178253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1610144dc2d0'
down_revision = 'c679e8f8b2d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_message_read_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_message_read_time')
    # ### end Alembic commands ###
