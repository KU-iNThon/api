from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.notice import Notice


class NoticeService:
    def __init__(self, engine: Engine):
        self.__engine = engine

    def save(self, session: Session, entity: Notice) -> Notice:
        session.add(entity)
        return entity
