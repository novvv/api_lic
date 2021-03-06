"""transaction_log

Revision ID: ca11a5c702c2
Revises: 17220f13141b
Create Date: 2019-01-22 13:55:03.330621

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = 'ca11a5c702c2'
down_revision = '17220f13141b'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction_log',
    sa.Column('transaction_log_uuid', sa.String(length=36), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('transaction_time', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('license_lrn_uuid', sa.String(length=36), nullable=True),
    sa.Column('license_switch_uuid', sa.String(length=36), nullable=True),
    sa.Column('type', api_lic.migration_types.ChoiceType({}), nullable=True),
    sa.Column('amount_lrn', api_lic.migration_types.Numeric(), server_default='0', nullable=False),
    sa.Column('amount_switch', api_lic.migration_types.Numeric(), server_default='0', nullable=False),
    sa.Column('transaction_id', sa.String(length=255), nullable=True),
    sa.Column('transaction_type', sa.String(length=255), nullable=True),
    sa.Column('from_ip', sa.String(length=36), nullable=True),
    sa.Column('transaction_src', sa.JSON(), nullable=True),
    sa.Column('status', api_lic.migration_types.ChoiceType({}), nullable=True),
    sa.Column('result', sa.Text(), nullable=True),
    sa.Column('payment_uuid', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['payment_uuid'], ['payment.payment_uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('transaction_log_uuid')
    )
    op.create_index(op.f('ix_transaction_log_payment_uuid'), 'transaction_log', ['payment_uuid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_transaction_log_payment_uuid'), table_name='transaction_log')
    op.drop_table('transaction_log')
    # ### end Alembic commands ###
