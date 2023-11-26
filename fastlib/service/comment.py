from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.comment import Comment
from fastlib.entity.notice import Notice
from fastlib.entity.group import Group
from fastlib.entity.user import User
from fastlib.entity.task import Task
from fastlib.entity.participant import Participant


class CommentService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        Comment.metadata.create_all(engine)
        Notice.metadata.create_all(engine)
        Group.metadata.create_all(engine)
        User.metadata.create_all(engine)
        Task.metadata.create_all(engine)
        Participant.metadata.create_all(engine)

    def save(self, session: Session, entity: Comment) -> Comment.id:
        session.add(entity)
        session.commit()
        return entity.id
