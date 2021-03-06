"""Initial migration.

Revision ID: 079723cf350e
Revises: 
Create Date: 2021-01-10 23:23:51.288565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079723cf350e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('transmission', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('img',
    sa.Column('img_id', sa.Integer(), nullable=False),
    sa.Column('auto_id', sa.Integer(), nullable=True),
    sa.Column('img_url', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['auto_id'], ['auto.id'], ),
    sa.PrimaryKeyConstraint('img_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('img')
    op.drop_table('auto')
    # ### end Alembic commands ###
