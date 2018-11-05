"""package switch sub type

Revision ID: d40606f1a9c0
Revises: cf0fe8ceaba4
Create Date: 2018-11-05 16:25:18.202260

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = 'd40606f1a9c0'
down_revision = 'cf0fe8ceaba4'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('package_switch', sa.Column('sub_type', api_lic.migration_types.ChoiceType({}), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('package_switch', 'sub_type')
    # ### end Alembic commands ###