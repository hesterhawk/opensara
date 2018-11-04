"""empty message

Revision ID: d79aaf6fd803
Revises: ac55dcbdaf3c
Create Date: 2018-11-03 17:12:26.394920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd79aaf6fd803'
down_revision = 'ac55dcbdaf3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('project_token_key', 'project', type_='unique')
    op.drop_column('project', 'token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('token', sa.VARCHAR(length=32), autoincrement=False, nullable=True))
    op.create_unique_constraint('project_token_key', 'project', ['token'])
    # ### end Alembic commands ###
