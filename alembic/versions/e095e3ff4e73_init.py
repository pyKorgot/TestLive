"""init

Revision ID: e095e3ff4e73
Revises: 
Create Date: 2024-01-29 16:31:22.026125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e095e3ff4e73'
down_revision: Union[str, None] = None


def upgrade() -> None:
    op.execute('create schema tests')
    op.create_table('t_test_plan',
    sa.Column('id_test_plan', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('name', sa.String(length=180), nullable=True, comment='Playback Steps'),
    sa.Column('id_parent', sa.Integer(), nullable=True, comment='ID Parent'),
    sa.ForeignKeyConstraint(['id_parent'], ['tests.t_test_plan.id_test_plan'], ),
    sa.PrimaryKeyConstraint('id_test_plan'),
    schema='tests',
    comment='Test Folder'
    )
    op.create_index(op.f('ix_tests_t_test_plan_id_parent'), 't_test_plan', ['id_parent'], unique=False, schema='tests')
    op.create_index(op.f('ix_tests_t_test_plan_id_test_plan'), 't_test_plan', ['id_test_plan'], unique=False, schema='tests')
    op.create_table('t_test_case',
    sa.Column('id_test_case', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('name', sa.String(180), nullable=False, comment='Name Test Case'),
    sa.Column('id_test_plan', sa.Integer(), nullable=True, comment='ID Test Plan'),
    sa.ForeignKeyConstraint(['id_test_plan'], ['tests.t_test_plan.id_test_plan'], ),
    sa.PrimaryKeyConstraint('id_test_case'),
    schema='tests',
    comment='Test Folder'
    )
    op.create_index(op.f('ix_tests_t_test_case_id_test_case'), 't_test_case', ['id_test_case'], unique=False, schema='tests')
    op.create_index(op.f('ix_tests_t_test_case_id_test_plan'), 't_test_case', ['id_test_plan'], unique=False, schema='tests')
    op.create_table('t_test_step',
    sa.Column('id_test_step', sa.Integer(), nullable=False, comment='ID'),
    sa.Column('id_test_case', sa.Integer(), nullable=True, comment='ID Test Case'),
    sa.Column('playback', sa.Text(), nullable=True, comment='Playback Steps'),
    sa.Column('excepted', sa.Text(), nullable=True, comment='Excepted Result'),
    sa.ForeignKeyConstraint(['id_test_case'], ['tests.t_test_case.id_test_case'], ),
    sa.PrimaryKeyConstraint('id_test_step'),
    schema='tests',
    comment='Test Folder'
    )
    op.create_index(op.f('ix_tests_t_test_step_id_test_step'), 't_test_step', ['id_test_step'], unique=False, schema='tests')


def downgrade() -> None:
    op.drop_index(op.f('ix_tests_t_test_step_id_test_step'), table_name='t_test_step', schema='tests')
    op.drop_table('t_test_step', schema='tests')
    op.drop_index(op.f('ix_tests_t_test_case_id_test_plan'), table_name='t_test_case', schema='tests')
    op.drop_index(op.f('ix_tests_t_test_case_id_test_case'), table_name='t_test_case', schema='tests')
    op.drop_table('t_test_case', schema='tests')
    op.drop_index(op.f('ix_tests_t_test_plan_id_test_plan'), table_name='t_test_plan', schema='tests')
    op.drop_index(op.f('ix_tests_t_test_plan_id_parent'), table_name='t_test_plan', schema='tests')
    op.drop_table('t_test_plan', schema='tests')
    op.execute('drop schema tests')
