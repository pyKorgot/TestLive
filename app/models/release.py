from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Release(Base):
    __tablename__ = 't_release'
    __table_args__ = ({'schema': 'tests', 'comment': 'Test Folder'})

    id_release = Column(Integer, primary_key=True, index=True, comment='ID')
    name = Column(String(180), nullable=False, comment='Name Release')