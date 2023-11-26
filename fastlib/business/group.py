from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker

from fastlib.business.model.group import (
    GroupNoticePostRequestDto,
    GroupNoticePostResponseDto,
    GroupParticipateResponseDto,
    GroupPostRecruitRequestDto,
    GroupPostRecruitResponseDto,
    GroupPostTaskRequestDto,
    GroupPostTaskResponseDto,
    GroupRegisterRequestDto,
    GroupRegisterResponseDto,
)
from fastlib.entity.group import Group
from fastlib.entity.notice import Notice
from fastlib.entity.participant import Participant
from fastlib.entity.recruit import Recruit
from fastlib.entity.task import Task
from fastlib.service.group import GroupService
from fastlib.service.notice import NoticeService
from fastlib.service.participant import ParticipantService
from fastlib.service.recruit import RecruitService
from fastlib.service.task import TaskService
from fastlib.service.user import UserService


class GroupBusiness:
    def __init__(
        self,
        session: sessionmaker,
        user_service: UserService,
        group_service: GroupService,
        participant_service: ParticipantService,
        recruit_service: RecruitService,
        notice_service: NoticeService,
        task_service: TaskService,
    ):
        self.__session = session
        self.__user_service = user_service
        self.__group_service = group_service
        self.__participant_service = participant_service
        self.__recruit_service = recruit_service
        self.__notice_service = notice_service
        self.__task_service = task_service

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
            authorized = False
            for p in group.participants:
                if p.user_id == user.id:
                    authorized = True
                    break
            if not authorized:
                raise HTTPException(status_code=403, detail="공지를 등록할 권한이 없습니다.")
            entity = Notice(group=group, user=user, title=req.title, description=req.description)
            entity = self.__notice_service.save(session=session, entity=entity)
            session.commit()
            res = GroupNoticePostResponseDto(id=entity.id)
        return res

    def participate(self, user_id: str, room_id: int) -> GroupParticipateResponseDto:
        """
        :return: room_id 반환
        """
        with self.__session() as session:
            user = self.__user_service.find(session=session, id_=user_id)
            group = self.__group_service.find(session=session, id_=room_id)
            is_exist = False
            for p in group.participants:
                if p.user_id == user.id:
                    is_exist = True
                    break
            if is_exist:
                raise HTTPException(status_code=409, detail="이미 참여한 모임입니다.")
            participant = Participant(user=user, group=group, role="user")
            self.__participant_service.save(session=session, entity=participant)
            session.commit()
            res = GroupParticipateResponseDto(id=participant.group_id)
        return res

    def create_task(self, user_id: str, room_id: int, req: GroupPostTaskRequestDto) -> GroupPostTaskResponseDto:
        with self.__session() as session:
            user = self.__user_service.find(session=session, id_=user_id)
            group = self.__group_service.find(session=session, id_=room_id)
            admin = next(filter(lambda p: p.role == "admin", group.participants), None)
            if not admin or admin.user_id != user.id:
                raise HTTPException(status_code=403, detail="활동은 관리자만 등록할 수 있습니다.")
            task = Task(group=group, title=req.title, start_date=req.start_date, end_date=req.end_date)
            task = self.__task_service.save(session=session, entity=task)
            session.commit()
            res = GroupPostTaskResponseDto(id=task.id)
        return res
