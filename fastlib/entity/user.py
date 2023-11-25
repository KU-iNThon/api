from sqlalchemy import Column, VARCHAR

from fastlib.entity.base import Base


class User(Base):
    __tablename__ = "users"
    id = Column(VARCHAR(20), primary_key=True, index=True)
    nickname = Column(VARCHAR(30))
    pw = Column(VARCHAR(30))
    region = Column(VARCHAR(50))
