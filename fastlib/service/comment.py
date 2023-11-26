from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.comment import Comment


class CommentService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        Comment.metadata.creat.all(engine)

    def save(self, session: Session, entity: Comment) -> Comment.id:
        session.add(entity)
        session.commit()
        return entity.id
