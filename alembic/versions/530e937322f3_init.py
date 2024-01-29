"""init

Revision ID: 530e937322f3
Revises: 
Create Date: 2024-01-29 18:20:37.090142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '530e937322f3'
down_revision: Union[str, None] = None


def upgrade() -> None:
    op.execute('create schema tests')


def downgrade() -> None:
    op.execute('drop schema tests')