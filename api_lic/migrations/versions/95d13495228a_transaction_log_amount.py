"""transaction_log amount

Revision ID: 95d13495228a
Revises: f11572091a96
Create Date: 2019-01-22 18:12:51.210901

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = '95d13495228a'
down_revision = 'f11572091a96'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction_log', sa.Column('amount_total', api_lic.migration_types.Numeric(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transaction_log', 'amount_total')
    # ### end Alembic commands ###