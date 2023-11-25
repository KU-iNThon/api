from sqlalchemy import Column, ForeignKey, Integer, TEXT, VARCHAR
from sqlalchemy.orm import relationship

from fastlib.entity.base import Base


class Recruit(Base):
    __tablename__ = "recruits"
    id = Column(Integer, ForeignKey("groups.id"), primary_key=True)
    title = Column(VARCHAR(50))
    description = Column(TEXT)
    tags = Column(TEXT)

    group = relationship("Group")
