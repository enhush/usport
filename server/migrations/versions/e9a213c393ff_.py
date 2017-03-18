"""empty message

Revision ID: e9a213c393ff
Revises: 
Create Date: 2017-03-18 14:12:17.655000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9a213c393ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_sport_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('createdOn', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updatedOn', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_sport_types')
    # ### end Alembic commands ###
