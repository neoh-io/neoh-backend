"""fix last_updated

Revision ID: d11f3ea5470c
Revises: f830888cb73e
Create Date: 2021-02-27 08:37:19.134726

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d11f3ea5470c"
down_revision = "f830888cb73e"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
ALTER TABLE youtube.video_mutable_metadata
    ALTER COLUMN last_updated SET DEFAULT now();
    """
    )
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
