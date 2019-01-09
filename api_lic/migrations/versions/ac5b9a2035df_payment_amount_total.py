"""payment amount_total

Revision ID: ac5b9a2035df
Revises: 82e5ccccac94
Create Date: 2019-01-07 13:36:05.927665

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = 'ac5b9a2035df'
down_revision = '82e5ccccac94'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payment', 'amount_total')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('amount_total', sa.NUMERIC(), server_default=sa.text("'0'::numeric"), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
