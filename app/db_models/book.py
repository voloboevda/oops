from app.db_models.base import Base
from sqlalchemy import  Column, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    author = Column(Text, nullable=False)
    issue_date = Column(DateTime(timezone=True), nullable=False)
    page_quantity = Column(Integer, nullable=False)
