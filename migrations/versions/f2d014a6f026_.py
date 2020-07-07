"""empty message

Revision ID: f2d014a6f026
Revises: 50a26b701259
Create Date: 2020-05-13 16:07:05.953765

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f2d014a6f026'
down_revision = '50a26b701259'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('description', sa.String(), nullable=True))
    op.add_column('events', sa.Column('planned_end', sa.DateTime(), nullable=True))
    op.add_column('events', sa.Column('planned_start', sa.DateTime(), nullable=True))
    op.add_column('events', sa.Column('estimated_duration', sa.Integer, nullable=True))
    op.drop_column('events', 'planned_date')
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
                    sa.Column('username', sa.String(), nullable=False, unique=True),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('_password', sa.Binary(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('planned_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('events', 'planned_start')
    op.drop_column('events', 'planned_end')
    op.drop_column('events', 'description')
    # ### end Alembic commands ###
