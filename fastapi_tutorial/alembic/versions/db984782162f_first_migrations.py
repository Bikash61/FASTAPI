"""first migrations

Revision ID: db984782162f
Revises: b26e516c7454
Create Date: 2024-09-13 16:47:44.780085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db984782162f'
down_revision: Union[str, None] = 'b26e516c7454'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
