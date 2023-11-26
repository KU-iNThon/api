from sqlachemy.orm import sessionmaker

from fastlib.service.group import GroupService
from fastlib.business.model.participant import GrouptParticipantResponseDto
from fastlib.entity.participant import Participant


class ParticipantBusiness:
    def __int__(
        self,
        session: sessionmaker,
        user_service: UserService,
        group_service: GroupService,
        participant_service: ParticipantService,
    ):
        self.__session = session
        self.__user_service = user_service
        self.__group_service = group_service
        self.__participant_service = participant_service

    def participate(self, user_id: str, group_id: int) -> GroupParticipantResponsedto:
        with self.__session() as session:
            entity = Participant(user_id=user_id, group_id=group_id, role="user")
            result = session.query(Participant).filter_by(id=user_id, group_id=group_id).first()
            if result is not None:
                raise HTTPException(status_code=409, detail="중복된 참여자입니다.")
            else:
                session.add(entity)
                session.commit()
                return group_id