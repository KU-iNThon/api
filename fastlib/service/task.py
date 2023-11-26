from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.task import Task


class TaskService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        Task.metadata.create_all(engine)

    def save(self, session: Session, entity: Task) -> Task.id:
        session.add(entity)
        session.commit()
        return entity.id
