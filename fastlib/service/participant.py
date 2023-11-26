from fastapi import HTTPException
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.group import Group
from fastlib.entity.participant import Participant
from fastlib.entity.user import User


class ParticipantService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        User.metadata.create_all(engine)
        Group.metadata.create_all(engine)
        Participant.metadata.create_all(engine)

    def save(self, session: Session, entity: Participant) -> Participant:
        if session.query(Participant).filter_by(group_id=entity.group_id, user_id=entity.user_id).first():
            raise HTTPException(status_code=409, detail="중복된 참여자입니다.")
        else:
            session.add(entity)
            res = session.query(Participant).filter_by(group_id=entity.group_id, user_id=entity.user_id).first()
            return res
