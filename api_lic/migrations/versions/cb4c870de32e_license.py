"""license

Revision ID: cb4c870de32e
Revises: d72cae15953e
Create Date: 2018-10-08 13:37:24.526175

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = 'cb4c870de32e'
down_revision = 'd72cae15953e'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rate',
    sa.Column('rate_uuid', sa.String(length=36), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('type', api_lic.migration_types.ChoiceType({}), nullable=True),
    sa.Column('rate', api_lic.migration_types.Numeric(), server_default='0', nullable=False),
    sa.PrimaryKeyConstraint('rate_uuid')
    )
    op.create_table('license',
    sa.Column('license_uuid', sa.String(length=36), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('rate_uuid', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['rate_uuid'], ['rate.rate_uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('license_uuid')
    )
    op.create_index(op.f('ix_license_rate_uuid'), 'license', ['rate_uuid'], unique=False)
    op.create_table('license_lrn',
    sa.Column('license_uuid', sa.String(length=36), nullable=True),
    sa.Column('cps', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['license_uuid'], ['license.license_uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('license_uuid')
    )
    op.create_index(op.f('ix_license_lrn_license_uuid'), 'license_lrn', ['license_uuid'], unique=False)
    op.create_table('license_period',
    sa.Column('license_period_uuid', sa.String(length=36), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('license_uuid', sa.String(length=36), nullable=True),
    sa.Column('user_uuid', sa.String(length=36), nullable=False),
    sa.Column('start_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('end_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('cost', api_lic.migration_types.Numeric(), server_default='0', nullable=False),
    sa.ForeignKeyConstraint(['license_uuid'], ['license.license_uuid'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.user_uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('license_period_uuid')
    )
    op.create_index(op.f('ix_license_period_license_uuid'), 'license_period', ['license_uuid'], unique=False)
    op.create_index(op.f('ix_license_period_user_uuid'), 'license_period', ['user_uuid'], unique=False)
    op.create_table('license_switch',
    sa.Column('license_uuid', sa.String(length=36), nullable=True),
    sa.Column('ip', sa.String(length=16), nullable=False),
    sa.ForeignKeyConstraint(['license_uuid'], ['license.license_uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('license_uuid')
    )
    op.create_index(op.f('ix_license_switch_license_uuid'), 'license_switch', ['license_uuid'], unique=False)
    op.create_table('notification',
    sa.Column('notification_uuid', sa.String(length=36), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('user_uuid', sa.String(length=36), nullable=True),
    sa.Column('subject', sa.String(length=64), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_on', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_uuid'], ['user.user_uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('notification_uuid')
    )
    op.create_index(op.f('ix_notification_user_uuid'), 'notification', ['user_uuid'], unique=False)
    op.create_table('payment',
    sa.Column('payment_uuid', sa.String(length=36), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('license_period_uuid', sa.String(length=36), nullable=True),
    sa.Column('amount', api_lic.migration_types.Numeric(), server_default='0', nullable=False),
    sa.Column('paid_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('type', api_lic.migration_types.ChoiceType({}), nullable=True),
    sa.ForeignKeyConstraint(['license_period_uuid'], ['license_period.license_period_uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('payment_uuid')
    )
    op.create_index(op.f('ix_payment_license_period_uuid'), 'payment', ['license_period_uuid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_payment_license_period_uuid'), table_name='payment')
    op.drop_table('payment')
    op.drop_index(op.f('ix_notification_user_uuid'), table_name='notification')
    op.drop_table('notification')
    op.drop_index(op.f('ix_license_switch_license_uuid'), table_name='license_switch')
    op.drop_table('license_switch')
    op.drop_index(op.f('ix_license_period_user_uuid'), table_name='license_period')
    op.drop_index(op.f('ix_license_period_license_uuid'), table_name='license_period')
    op.drop_table('license_period')
    op.drop_index(op.f('ix_license_lrn_license_uuid'), table_name='license_lrn')
    op.drop_table('license_lrn')
    op.drop_index(op.f('ix_license_rate_uuid'), table_name='license')
    op.drop_table('license')
    op.drop_table('rate')
    # ### end Alembic commands ###
