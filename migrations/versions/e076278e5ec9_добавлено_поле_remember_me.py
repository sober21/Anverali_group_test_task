"""добавлено поле remember_me

Revision ID: e076278e5ec9
Revises: ef9eabf580a6
Create Date: 2024-04-25 23:23:17.371701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e076278e5ec9'
down_revision = 'ef9eabf580a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('remember_me', sa.String(length=1000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('remember_me')

    # ### end Alembic commands ###
