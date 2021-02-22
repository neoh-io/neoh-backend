from sqlalchemy import Column, Integer, Text

from neoh_backend.db.base_class import Base


class Video(Base):
    __tablename__ = "video"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    youtube_video_id = Column(Text, index=True, nullable=False)
    title = Column(Text, nullable=False)

    __table_args__ = {"schema": "youtube"}
