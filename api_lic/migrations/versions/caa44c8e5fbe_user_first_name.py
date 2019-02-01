"""user first_name

Revision ID: caa44c8e5fbe
Revises: ac5b9a2035df
Create Date: 2019-01-07 13:54:14.814135

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = 'caa44c8e5fbe'
down_revision = 'ac5b9a2035df'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=32), nullable=True))
    op.create_index(op.f('ix_user_first_name'), 'user', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_first_name'), table_name='user')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###