from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, VARCHAR
from sqlalchemy.orm import relationship

from fastlib.entity.base import Base


class Participant(Base):
    __tablename__ = "participants"
    user_id = Column(VARCHAR(20), ForeignKey("users.id"), primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)
    role = Column(VARCHAR(10))
    user = relationship("User")
    group = relationship("Group", back_populates="participants")
    __table_args__ = (CheckConstraint("role IN ('admin', 'user')", name="role_check"),)
