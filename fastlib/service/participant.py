from fastapi import HTTPException
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.participant import Participant


class ParticipantService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        Participant.metadata.create_all(engine)

    def participant(self, group_id: int, session: Session, entity: Participant) -> Participant:
        if session.query(Participant).filter_by(entity.group_id == group_id, entity.user_id == id):
            raise HTTPException(status_code=409, detail="중복된 사용자입니다.")
        else:
            session.add(entity)
            res = session.query(Participant).filter_by(id=entity.id).first()
            session.commit()
            return res
