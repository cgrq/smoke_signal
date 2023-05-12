"""empty message

Revision ID: c60fa86303fc
Revises: cc595a261d4c
Create Date: 2023-05-11 18:13:16.174352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c60fa86303fc'
down_revision = 'cc595a261d4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('channels', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=500),
               existing_nullable=True)

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('message',
               existing_type=sa.VARCHAR(length=700),
               type_=sa.String(length=800),
               existing_nullable=True)

    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=500),
               existing_nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('hashed_password',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=500),
               existing_nullable=False)
        batch_op.alter_column('profile_image_url',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('profile_image_url',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('hashed_password',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)

    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('message',
               existing_type=sa.String(length=800),
               type_=sa.VARCHAR(length=700),
               existing_nullable=True)

    with op.batch_alter_table('channels', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)

    # ### end Alembic commands ###