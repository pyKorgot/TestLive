from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class TestStatus(Base):
    __tablename__ = 't_test_status'
    __table_args__ = ({'schema': 'tests', 'comment': 'Test Folder'})

    id_test_status = Column(Integer, primary_key=True, index=True, comment='ID')
    code_status = Column(String(50), comment='Code Status')
    name_status = Column(String(50), comment='Name Status')
