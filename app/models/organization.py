from sqlalchemy import Column, Integer, ForeignKey, String

from app.db.base_class import Base


class Organization(Base):
    __tablename__ = 't_organization'
    __table_args__ = ({'schema': 'tests', 'comment': 'Organization Table'})

    id_organization = Column(Integer, primary_key=True, index=True, comment='ID')
    name_organization = Column(String, comment='Name Organization')
