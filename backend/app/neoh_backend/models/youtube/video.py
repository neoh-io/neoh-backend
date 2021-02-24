from sqlalchemy import Column, Text
from sqlalchemy.orm import relationship

from neoh_backend.db.base_class import Base


class Video(Base):
    __tablename__ = "video"
    __table_args__ = {"schema": "youtube"}

    yt8m_id = Column(
        Text,
        nullable=True,
        unique=True,
        comment="See: http://research.google.com/youtube8m/video_id_conversion.html",
    )
    youtube_video_id = Column(
        Text, nullable=False, unique=True, comment="Unique Youtube Video ID"
    )
    title = Column(Text, nullable=False)

    video_mutable_metadata = relationship(
        "youtube.video_mutable_metadata", uselist=False, back_populates=False
    )
