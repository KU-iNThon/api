from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker

from fastlib.business.model.group import (
    GroupNoticePostRequestDto,
    GroupNoticePostResponseDto,
    GroupPostRecruitRequestDto,
    GroupPostRecruitResponseDto,
    GroupRegisterRequestDto,
    GroupRegisterResponseDto,
)
from fastlib.entity.group import Group
from fastlib.entity.participant import Participant
from fastlib.entity.recruit import Recruit
from fastlib.service.group import GroupService
from fastlib.service.participant import ParticipantService
from fastlib.service.recruit import RecruitService
from fastlib.service.user import UserService


class GroupBusiness:
    def __init__(
        self,
        session: sessionmaker,
        user_service: UserService,
        group_service: GroupService,
        participant_service: ParticipantService,
        recruit_service: RecruitService,
    ):
        self.__session = session
        self.__user_service = user_service
        self.__group_service = group_service
        self.__participant_service = participant_service
        self.__recruit_service = recruit_service

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

    def create_recruit(
        self, user_id: str, group_id: int, req: GroupPostRecruitRequestDto
    ) -> GroupPostRecruitResponseDto:
        with self.__session() as session:
            user = self.__user_service.find(session=session, id_=user_id)
            group = self.__group_service.find(session=session, id_=group_id)
            authorized = False
            for p in group.participants:
                if p.role == "admin" and p.user_id == user.id:
                    authorized = True
                    break
            if not authorized:
                raise HTTPException(status_code=403, detail="관리자만 등록할 수 있습니다.")

            entity = Recruit(group=group, title=req.title, description=req.description, tags=",".join(req.tags))
            entity = self.__recruit_service.save(session=session, entity=entity)
            session.commit()
            res = GroupPostRecruitResponseDto(id=entity.id)
        return res

    def create_notice(self, group_id: int, user_id: str, req: GroupNoticePostRequestDto) -> GroupNoticePostResponseDto:
        with self.__session() as session:
            group = self.__group_service.find(session=session, id_=group_id)
            user = self.__user_service.find(session=session, id_=user_id)
