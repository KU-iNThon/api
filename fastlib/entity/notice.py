from sqlalchemy import Column, ForeignKey, Integer, TEXT, UniqueConstraint, VARCHAR
from sqlalchemy.orm import relationship

from fastlib.entity.base import Base


class Notice(Base):
    __tablename__ = "notices"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    user_id = Column(VARCHAR(20), ForeignKey("users.id"))
    title = Column(VARCHAR(50))
    description = Column(TEXT)

    group = relationship("Group")
    user = relationship("User")
    __table_args__ = (UniqueConstraint("group_id", "user_id"),)
