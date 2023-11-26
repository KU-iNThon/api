from sqlalchemy import CheckConstraint, Column, VARCHAR

from fastlib.entity.base import Base


class TaskStatus(Base):
    __tablename__ = "task_statuses"
    id = Column(VARCHAR(10), primary_key=True, index=True)
    __table_args__ = CheckConstraint("id in ('PENDING', 'ACCEPTED')")
