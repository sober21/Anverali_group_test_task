"""empty message

Revision ID: e86c0eff9ac0
Revises: 8a2fa6b3f7cf
Create Date: 2024-04-23 17:06:21.151999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e86c0eff9ac0'
down_revision = '8a2fa6b3f7cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('klass_user', sa.String(length=15), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('klass_user')

    # ### end Alembic commands ###
