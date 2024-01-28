"""init

Revision ID: 38ba2c533b51
Revises: 
Create Date: 2024-01-28 15:34:03.659704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '38ba2c533b51'
down_revision: Union[str, None] = None


def upgrade() -> None:
    op.execute('create schema tests')

    op.create_table('t_test_case',
    sa.Column('id_test', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('playback', sa.Text(), nullable=True, comment='Playback Steps'),
    sa.Column('excepted', sa.Text(), nullable=True, comment='Excepted Result'),
    sa.PrimaryKeyConstraint('id_test'),
    schema='tests',
    comment='Test Folder'
    )
    op.create_index(op.f('ix_tests_t_test_case_id_test'), 't_test_case', ['id_test'], unique=False, schema='tests')


def downgrade() -> None:
    op.drop_index(op.f('ix_tests_t_test_case_id_test'), table_name='t_test_case', schema='tests')
    op.drop_table('t_test_case', schema='tests')
    
    op.execute('drop schema tests')
