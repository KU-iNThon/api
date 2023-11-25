from sqlalchemy import Column, ForeignKey, Integer, TEXT, VARCHAR
from sqlalchemy.orm import relationship

from fastlib.entity.base import Base


class Notice(Base):
    __tablename__ = "notices"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), primary_key=True)
    user_id = Column(VARCHAR(20), ForeignKey("users.id"), primary_key=True)
    title = Column(VARCHAR(50))
    description = Column(TEXT)

    group = relationship("Group")
    user = relationship("User")
