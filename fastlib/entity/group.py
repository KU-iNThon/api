from sqlalchemy import Column, Integer, TEXT, VARCHAR

from fastlib.entity.base import Base


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(VARCHAR(20))
    description = Column(TEXT)
    max_people = Column(Integer)
