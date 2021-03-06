"""payment lrn switch amount

Revision ID: 6fa1546cba13
Revises: cfa25697d301
Create Date: 2018-11-29 20:37:55.926680

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = '6fa1546cba13'
down_revision = 'cfa25697d301'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('amount_lrn', api_lic.migration_types.Numeric(), server_default='0', nullable=False))
    op.add_column('payment', sa.Column('amount_switch', api_lic.migration_types.Numeric(), server_default='0', nullable=False))
    op.add_column('payment', sa.Column('amount_total', api_lic.migration_types.Numeric(), server_default='0', nullable=False))
    op.drop_column('payment', 'amount')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('amount', sa.NUMERIC(), server_default=sa.text("'0'::numeric"), autoincrement=False, nullable=False))
    op.drop_column('payment', 'amount_total')
    op.drop_column('payment', 'amount_switch')
    op.drop_column('payment', 'amount_lrn')
    # ### end Alembic commands ###
