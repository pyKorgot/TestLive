from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base_class import Base


class TestCase(Base):
    __tablename__ = 't_test_case'
    __table_args__ = ({'schema': 'tests', 'comment': 'Test Folder'})

    id_test_case = Column(Integer, primary_key=True, index=True, comment='ID')
    id_test_plan = Column(Integer, ForeignKey('tests.t_test_plan.id_test_plan'), index=True, comment='ID Test Plan')
    name = Column(String(180), nullable=False, comment='Name')
