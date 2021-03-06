"""Created a table for pleblist songs

Revision ID: 2e647f0995
Revises: e54fed8855
Create Date: 2015-12-04 00:45:08.643028

"""

# revision identifiers, used by Alembic.
revision = '2e647f0995'
down_revision = 'e54fed8855'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_pleblist_song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_id', sa.Integer(), nullable=False),
    sa.Column('youtube_id', sa.String(length=64), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=False),
    sa.Column('date_played', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stream_id'], ['tb_stream.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tb_pleblist_song_stream_id'), 'tb_pleblist_song', ['stream_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tb_pleblist_song_stream_id'), table_name='tb_pleblist_song')
    op.drop_table('tb_pleblist_song')
    ### end Alembic commands ###
