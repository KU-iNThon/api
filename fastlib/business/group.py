from sqlalchemy.orm import sessionmaker

from fastlib.business.model.group import GroupRegisterRequestDto, GroupRegisterResponseDto
from fastlib.entity.group import Group
from fastlib.entity.participant import Participant
from fastlib.service.group import GroupService
from fastlib.service.participant import ParticipantService
from fastlib.service.user import UserService


class GroupBusiness:
    def __init__(
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

    def create(self, user_id: str, req: GroupRegisterRequestDto) -> GroupRegisterResponseDto:
        with self.__session() as session:
            user = self.__user_service.find(session=session, id_=user_id)
            group = Group(name=req.name, description=req.description, max_people=10)
            self.__group_service.save(session, group)
            participant = Participant(user=user, group=group, role="admin")
            self.__participant_service.save(session=session, entity=participant)
            session.commit()
            res = GroupRegisterResponseDto(id=group.id)
        return res
