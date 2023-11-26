from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException

from fastlib.service.participant import ParticipantService
from fastlib.business.model.participant import GroupParticipantResponseDto
from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker

from fastlib.entity.participant import Participant
from fastlib.service.group import GroupService
from fastlib.service.participant import ParticipantService
from fastlib.service.user import UserService
from fastlib.view.model.group import GroupParticipantResponseDto


class ParticipantBusiness:
    def __init__(self, session: sessionmaker):
        self.__session = session

    def participate(self, user_id: str, group_id: int) -> GroupParticipantResponseDto:
        with self.__session() as session:
            entity = Participant(user_id=user_id, group_id=group_id, role="user")
            result = session.query(Participant).filter_by(id=user_id, group_id=group_id).first()
            if result is not None:
                raise HTTPException(status_code=409, detail="중복된 참여자입니다.")
            else:
                session.add(entity)
                session.commit()
        return GroupParticipantResponseDto(id=entity.id)
