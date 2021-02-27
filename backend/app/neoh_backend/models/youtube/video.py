from sqlalchemy import Boolean, Column, Text
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
    youtube_video_id = Column(Text, unique=True, comment="Unique Youtube Video ID")
    title = Column(Text)
    private = Column(Boolean, comment="true if unable to access true youtube video id")
    embeddable = Column(Boolean)

    video_mutable_metadata = relationship(
        "youtube.video_mutable_metadata", uselist=False, back_populates=False
    )
