from sqlalchemy import Column, DateTime, ForeignKey, Integer, VARCHAR
from sqlalchemy.orm import relationship

from fastlib.entity.base import Base


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)
    title = Column(VARCHAR(20))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    group = relationship("Group")
