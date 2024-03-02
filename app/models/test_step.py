from sqlalchemy import Column, ForeignKey, Integer, Text

from app.db.base_class import Base


class TestStep(Base):
    __tablename__ = 't_test_step'
    __table_args__ = ({'schema': 'tests', 'comment': 'Test Folder'})

    id_test_step = Column(Integer, primary_key=True, index=True, comment='ID')
    id_test_case = Column(Integer, ForeignKey('tests.t_test_case.id_test_case'), comment='ID Test Case')

    number_step = Column(Integer, comment='Number Step')
    name_step = Column(Text, comment='Name Step')
    playback = Column(Text, comment='Playback Steps')
    excepted = Column(Text, comment='Excepted Result')
