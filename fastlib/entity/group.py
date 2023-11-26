from sqlalchemy import Column, Integer, TEXT, VARCHAR
from sqlalchemy.orm import relationship

from fastlib.entity.base import Base


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(VARCHAR(20))
    description = Column(TEXT)
    max_people = Column(Integer)
    participants = relationship("Participant", back_populates="group")

    recruit = relationship("Recruit", back_populates="group")
