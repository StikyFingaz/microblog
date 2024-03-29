"""user tokens

Revision ID: 78eb9043f1b2
Revises: bf61a6f2d17e
Create Date: 2021-05-07 17:03:07.665231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78eb9043f1b2'
down_revision = 'bf61a6f2d17e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###
