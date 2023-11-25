from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, TEXT, VARCHAR
from sqlalchemy.orm import relationship

from fastlib.entity.base import Base


class Comment(Base):
    __tablename__ = "commnents"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(VARCHAR(20), ForeignKey("users.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)
    notice_id = Column(Integer, ForeignKey("notices.id"), nullable=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    text = Column(TEXT)
    wrote_date = Column(DateTime, default=datetime.utcnow())

    user = relationship("User")
    group = relationship("Group")
    notice = relationship("Notice")
    task = relationship("Task")
