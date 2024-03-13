"""Add Product ecoscore_grade field

Revision ID: 7055fe5b4775
Revises: d98171064c5a
Create Date: 2024-03-09 12:54:14.104481

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7055fe5b4775"
down_revision: Union[str, None] = "d98171064c5a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("products", sa.Column("ecoscore_grade", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("products", "ecoscore_grade")
    # ### end Alembic commands ###
