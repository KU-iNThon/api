from sqlalchemy import Column, Integer, TEXT, VARCHAR
from sqlalchemy.orm import Mapped, relationship

from fastlib.entity.base import Base
from fastlib.entity.recruit import Recruit


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(20))
    description = Column(TEXT)
    max_people = Column(Integer)
    participants = relationship("Participant", back_populates="group")

    recruit: Mapped["Recruit"] = relationship("Recruit", back_populates="group")
    notices = relationship("Notice", back_populates="group")
    tasks = relationship("Task", back_populates="group")
