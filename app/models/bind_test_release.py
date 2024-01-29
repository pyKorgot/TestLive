from sqlalchemy import Column, Integer, ForeignKey

from app.db.base_class import Base


class BindTestRelease(Base):
    __tablename__ = 't_bind_test_release'
    __table_args__ = ({'schema': 'tests', 'comment': 'Bind Test Release'})

    id_bind_test_release = Column(Integer, primary_key=True, index=True, comment='ID')
    id_release = Column(Integer, ForeignKey('tests.t_release.id_release'), index=True, comment='ID Release')
    id_test_case = Column(Integer, ForeignKey('tests.t_test_case.id_test_case'), index=True, comment='ID Test Case')
