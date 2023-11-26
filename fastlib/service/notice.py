from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.group import Group
from fastlib.entity.notice import Notice
from fastlib.entity.user import User


class NoticeService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        Group.metadata.create_all(engine)
        User.metadata.create_all(engine)
        Notice.metadata.create_all(engine)

    def save(self, session: Session, entity: Notice) -> Notice:
        session.add(entity)
        return entity
