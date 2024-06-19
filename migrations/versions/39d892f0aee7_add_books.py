"""add books

Revision ID: 39d892f0aee7
Revises: 
Create Date: 2024-06-19 21:51:43.276503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39d892f0aee7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        '''
        create table books(
            id uuid primary key,
            created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
            updated_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
            title text not null,
            description text not null,
            author text not null,
            issue_date date not null,
            page_quantity integer not null        
        );
        '''
    )


def downgrade():
    raise NotImplementedError
