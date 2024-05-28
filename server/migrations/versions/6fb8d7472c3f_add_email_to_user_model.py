"""Add email to User model

Revision ID: 6fb8d7472c3f
Revises: f880b0c8443a
Create Date: 2024-05-28 11:44:44.420545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fb8d7472c3f'
down_revision = 'f880b0c8443a'
branch_labels = None
depends_on = None

def upgrade():
    # Add a name to the unique constraint
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=100), nullable=False))
        batch_op.create_unique_constraint('unique_email', ['email'])  # Provide a name for the unique constraint

def downgrade():
    # Drop the unique constraint by name
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('unique_email', type_='unique')  # Use the name of the unique constraint to drop it
        batch_op.drop_column('email')
