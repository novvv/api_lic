"""payment user_uuid

Revision ID: 802754132737
Revises: 56c8b65dd6a3
Create Date: 2018-10-24 23:12:29.899849

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = '802754132737'
down_revision = '56c8b65dd6a3'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('payment', sa.Column('user_uuid', sa.String(length=36), nullable=True))
    op.create_index(op.f('ix_payment_user_uuid'), 'payment', ['user_uuid'], unique=False)
    op.create_foreign_key(None, 'payment', 'user', ['user_uuid'], ['user_uuid'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'payment', type_='foreignkey')
    op.drop_index(op.f('ix_payment_user_uuid'), table_name='payment')
    op.drop_column('payment', 'user_uuid')
    op.drop_column('payment', 'description')
    # ### end Alembic commands ###
