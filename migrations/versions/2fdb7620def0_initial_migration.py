"""Initial Migration.

Revision ID: 2fdb7620def0
Revises: 083ab6b50593
Create Date: 2022-05-11 07:39:32.250165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fdb7620def0'
down_revision = '083ab6b50593'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('downvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('downVote', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('upvotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('upvote', sa.Integer(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('comments', sa.Column('date_posted', sa.DateTime(timezone=250), nullable=True))
    op.drop_column('comments', 'votes')
    op.add_column('pitch', sa.Column('date', sa.DateTime(timezone=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitch', 'date')
    op.add_column('comments', sa.Column('votes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('comments', 'date_posted')
    op.drop_table('upvotes')
    op.drop_table('downvotes')
    # ### end Alembic commands ###
