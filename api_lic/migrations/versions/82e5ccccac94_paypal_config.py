"""paypal config

Revision ID: 82e5ccccac94
Revises: 5a18f169eb3c
Create Date: 2018-12-20 18:03:05.244945

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = '82e5ccccac94'
down_revision = '5a18f169eb3c'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('config_payment', sa.Column('paypal_email', sa.String(length=64), nullable=True))
    op.add_column('config_payment', sa.Column('paypal_pkey', sa.String(length=128), nullable=True))
    op.add_column('config_payment', sa.Column('paypal_skey', sa.String(length=128), nullable=True))
    op.add_column('config_payment', sa.Column('paypal_svc_charge', api_lic.migration_types.Numeric(), nullable=True))
    op.add_column('config_payment', sa.Column('paypal_test_mode', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('config_payment', 'paypal_test_mode')
    op.drop_column('config_payment', 'paypal_svc_charge')
    op.drop_column('config_payment', 'paypal_skey')
    op.drop_column('config_payment', 'paypal_pkey')
    op.drop_column('config_payment', 'paypal_email')
    # ### end Alembic commands ###
