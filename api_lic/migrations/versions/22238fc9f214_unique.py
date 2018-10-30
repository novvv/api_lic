"""unique

Revision ID: 22238fc9f214
Revises: e19d1c7311c9
Create Date: 2018-10-30 20:02:58.285591

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = '22238fc9f214'
down_revision = 'e19d1c7311c9'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_license_lrn_package_lrn_uuid_user_uuid', 'license_lrn', ['package_lrn_uuid', 'user_uuid'])
    op.create_unique_constraint('uq_license_switch_package_switch_uuid_user_uuid', 'license_switch', ['package_switch_uuid', 'user_uuid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_license_switch_package_switch_uuid_user_uuid', 'license_switch', type_='unique')
    op.drop_constraint('uq_license_lrn_package_lrn_uuid_user_uuid', 'license_lrn', type_='unique')
    # ### end Alembic commands ###
