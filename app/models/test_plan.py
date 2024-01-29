from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base_class import Base


class TestPlan(Base):
    __tablename__ = 't_test_plan'
    __table_args__ = ({'schema': 'tests', 'comment': 'Test Folder'})

    id_test_plan = Column(Integer, primary_key=True, index=True, comment='ID')
    name = Column(String(180), comment='Playback Steps')
    id_parent = Column(Integer, ForeignKey('tests.t_test_plan.id_test_plan'), index=True, comment='ID Parent')
