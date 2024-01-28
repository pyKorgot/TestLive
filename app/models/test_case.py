from sqlalchemy import Column, Integer, Text

from app.db.base_class import Base


class TestCase(Base):
    __tablename__ = 't_test_case'
    __table_args__ = ({'schema': 'tests', 'comment': 'Test Folder'})

    id_test = Column(Integer, primary_key=True, index=True, comment='ID')
    playback = Column(Text, comment='Playback Steps')
    excepted = Column(Text, comment='Excepted Result')
