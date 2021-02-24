from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import relationship

from neoh_backend.db.base_class import Base

video_yt8m_vocabulary_map = Table(
    "video_yt8m_vocabulary_map",
    Base.metadata,
    Column(
        "video_id", Integer, ForeignKey("youtube.video.id"), unique=True, nullable=False
    ),
    Column(
        "yt8m_vocabulary_id",
        Integer,
        ForeignKey("youtube.yt8m_vocabulary.id"),
        unique=True,
        nullable=False,
    ),
    schema="youtube",
)


class YT8MVocabulary(Base):
    __tablename__ = "yt8m_vocabulary"
    __table_args__ = {"schema": "youtube"}

    index = Column(
        Integer,
        unique=True,
        nullable=False,
        comment="the index as defined by the vocabulary file",
    )
    knowledge_graph_id = Column(Text)
    name = Column(Text, unique=True, nullable=False)
    wiki_url = Column(Text)
    vertical_id_1 = Column(Integer, ForeignKey("youtube.yt8m_vertical.id"))
    vertical_id_2 = Column(Integer, ForeignKey("youtube.yt8m_vertical.id"))
    vertical_id_3 = Column(Integer, ForeignKey("youtube.yt8m_vertical.id"))

    video = relationship("youtube.Video", secondary=video_yt8m_vocabulary_map)
    vertical_1 = relationship("youtube.yt8m_vertical", foreign_keys=[vertical_id_1])
    vertical_2 = relationship("youtube.yt8m_vertical", foreign_keys=[vertical_id_2])
    vertical_3 = relationship("youtube.yt8m_vertical", foreign_keys=[vertical_id_3])
