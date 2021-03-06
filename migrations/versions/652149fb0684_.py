"""empty message

Revision ID: 652149fb0684
Revises: f64210f56dbe
Create Date: 2021-03-06 20:20:51.350155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '652149fb0684'
down_revision = 'f64210f56dbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
