"""config_payment

Revision ID: a0ecabe25ded
Revises: d74fb65a2c6c
Create Date: 2018-11-23 20:18:43.816115

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = 'a0ecabe25ded'
down_revision = 'd74fb65a2c6c'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config_payment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('charge_type', api_lic.migration_types.ChoiceType({}), nullable=True),
    sa.Column('stripe_email', sa.String(length=64), nullable=True),
    sa.Column('stripe_skey', sa.String(length=64), nullable=True),
    sa.Column('stripe_pkey', sa.String(length=64), nullable=True),
    sa.Column('stripe_svc_charge', sa.Integer(), nullable=True),
    sa.Column('stripe_test_mode', sa.Boolean(), nullable=True),
    sa.Column('confirm_enabled', sa.Boolean(), nullable=True),
    sa.Column('email_confirm_to', sa.String(length=64), nullable=True),
    sa.Column('notification_enabled', sa.Boolean(), nullable=True),
    sa.Column('email_cc_to', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('config_payment')
    # ### end Alembic commands ###
