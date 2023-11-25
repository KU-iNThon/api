from sqlalchemy import Column, ForeignKey, Integer, VARCHAR
from sqlalchemy.orm import relationship

from fastlib.entity.base import Base


class ParticipantsTasks(Base):
    __tablename__ = "participants_tasks"
    task_id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)
    user_id = Column(VARCHAR(20), ForeignKey("users.id"), primary_key=True)
    status_id = Column(VARCHAR(10), ForeignKey("task_statuses.id"))

    task = relationship("Task")
    group = relationship("Group")
    user = relationship("User")
    status = relationship("TaskStatus")
