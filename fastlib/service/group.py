from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.group import Group


class GroupService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        Group.metadata.create_all(engine)

    def save(self, session: Session, entity: Group) -> Group:
        session.add(entity)
        session.commit()
        return entity
