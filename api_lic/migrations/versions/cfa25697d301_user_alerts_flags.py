"""user alerts flags

Revision ID: cfa25697d301
Revises: 27aa3eebd22c
Create Date: 2018-11-28 00:44:54.685318

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = 'cfa25697d301'
down_revision = '27aa3eebd22c'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('alert_license_expired', sa.Boolean(), server_default='true', nullable=True))
    op.add_column('user', sa.Column('alert_license_purchased', sa.Boolean(), server_default='true', nullable=True))
    op.add_column('user', sa.Column('alert_license_will_expired', sa.Boolean(), server_default='true', nullable=True))
    op.add_column('user', sa.Column('alert_payment_received', sa.Boolean(), server_default='true', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'alert_payment_received')
    op.drop_column('user', 'alert_license_will_expired')
    op.drop_column('user', 'alert_license_purchased')
    op.drop_column('user', 'alert_license_expired')
    # ### end Alembic commands ###