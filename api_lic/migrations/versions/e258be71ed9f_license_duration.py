"""license duration

Revision ID: e258be71ed9f
Revises: 98ce186d11f2
Create Date: 2018-12-07 02:24:41.566507

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = 'e258be71ed9f'
down_revision = '98ce186d11f2'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('license_lrn', sa.Column('duration', api_lic.migration_types.ChoiceType({}), server_default='1', nullable=True))
    op.add_column('license_switch', sa.Column('duration', api_lic.migration_types.ChoiceType({}), server_default='1', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('license_switch', 'duration')
    op.drop_column('license_lrn', 'duration')
    # ### end Alembic commands ###