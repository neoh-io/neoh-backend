from sqlalchemy import Column, Computed, ForeignKey, Integer, SmallInteger, Table, Text
from sqlalchemy.orm import relationship

from neoh_backend.db.base_class import Base


class YT8MVertical(Base):
    __tablename__ = "yt8m_vertical"
    __table_args__ = {"schema": "youtube"}

    name = Column(Text, unique=True, nullable=False)
