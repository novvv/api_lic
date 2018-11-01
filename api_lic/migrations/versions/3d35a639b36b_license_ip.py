"""license ip

Revision ID: 3d35a639b36b
Revises: 22238fc9f214
Create Date: 2018-11-01 19:45:32.610974

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = '3d35a639b36b'
down_revision = '22238fc9f214'
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()
    connection.execute('delete from license_lrn')
    connection.execute('delete from license_switch')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('license_lrn', sa.Column('ip', sa.String(length=16), nullable=False))
    op.create_index(op.f('ix_license_lrn_ip'), 'license_lrn', ['ip'], unique=False)
    op.drop_index('ix_license_lrn_plan_uuid', table_name='license_lrn')
    op.drop_constraint('license_lrn_plan_uuid_fkey', 'license_lrn', type_='foreignkey')
    op.drop_column('license_lrn', 'plan_uuid')
    op.add_column('license_switch', sa.Column('ip', sa.String(length=16), nullable=False))
    op.create_index(op.f('ix_license_switch_ip'), 'license_switch', ['ip'], unique=False)
    op.drop_index('ix_license_switch_plan_uuid', table_name='license_switch')
    op.drop_constraint('license_switch_plan_uuid_fkey', 'license_switch', type_='foreignkey')
    op.drop_column('license_switch', 'plan_uuid')
    op.drop_column('package_lrn', 'lrn_ip')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('package_lrn', sa.Column('lrn_ip', sa.VARCHAR(length=16), autoincrement=False, nullable=False))
    op.add_column('license_switch', sa.Column('plan_uuid', sa.VARCHAR(length=36), autoincrement=False, nullable=True))
    op.create_foreign_key('license_switch_plan_uuid_fkey', 'license_switch', 'plan', ['plan_uuid'], ['plan_uuid'], ondelete='CASCADE')
    op.create_index('ix_license_switch_plan_uuid', 'license_switch', ['plan_uuid'], unique=False)
    op.drop_index(op.f('ix_license_switch_ip'), table_name='license_switch')
    op.drop_column('license_switch', 'ip')
    op.add_column('license_lrn', sa.Column('plan_uuid', sa.VARCHAR(length=36), autoincrement=False, nullable=True))
    op.create_foreign_key('license_lrn_plan_uuid_fkey', 'license_lrn', 'plan', ['plan_uuid'], ['plan_uuid'], ondelete='CASCADE')
    op.create_index('ix_license_lrn_plan_uuid', 'license_lrn', ['plan_uuid'], unique=False)
    op.drop_index(op.f('ix_license_lrn_ip'), table_name='license_lrn')
    op.drop_column('license_lrn', 'ip')
    # ### end Alembic commands ###