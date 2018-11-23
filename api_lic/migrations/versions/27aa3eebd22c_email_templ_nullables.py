"""email templ nullables

Revision ID: 27aa3eebd22c
Revises: a0ecabe25ded
Create Date: 2018-11-23 21:15:14.526639

"""
from alembic import op
import sqlalchemy as sa
import api_lic.migration_types


# revision identifiers, used by Alembic.
revision = '27aa3eebd22c'
down_revision = 'a0ecabe25ded'
branch_labels = None
depends_on = None


def upgrade():
    #connection = op.get_bind()
    #connection.execute('delete from users')
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('email_template', 'content_html',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('email_template', 'content_text',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('email_template', 'hint',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('email_template', 'hint',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('email_template', 'content_text',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('email_template', 'content_html',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
