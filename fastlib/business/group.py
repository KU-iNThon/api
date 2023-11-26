from sqlalchemy.orm import sessionmaker

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
