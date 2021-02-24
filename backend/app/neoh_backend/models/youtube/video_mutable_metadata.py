from sqlalchemy import Column, Computed, ForeignKey, Integer, SmallInteger
from sqlalchemy.orm import relationship

from neoh_backend.db.base_class import Base


class VideoMutableMetadata(Base):
    __tablename__ = "video_mutable_metadata"
    __table_args__ = {"schema": "youtube"}

    video_id = Column(
        Integer, ForeignKey("youtube.video.id"), unique=True, nullable=False
    )
    views = Column(Integer, comment="number of views of the video")
    view_magnitude = Column(
        SmallInteger,
        Computed("CEIL(LOG(views))"),
        comment="order of magnitude of the 'views' column",
    )

    video = relationship("youtube.video", back_populates="video")