from fastapi import APIRouter, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.base import Base


from fastlib.service.participant import ParticipantService
from fastlib.view.model.api import ApiResponse
from fastlib.view.model.group import (
    GroupAdminResponseDto,
    GroupCommentPostRequestDto,
    GroupCommentPostResponseDto,
    GroupDetailResponseDto,
    GroupNoticeCommentResponseDto,
    GroupNoticeDetailResponseDto,
    GroupNoticePostRequestDto,
    GroupNoticePostResponseDto,
    GroupNoticeResponseDto,
    GroupParticipantResponseDto,
    GroupParticipateResponseDto,
    GroupPostRecruitRequestDto,
    GroupPostRecruitResponseDto,
    GroupPostTaskRequestDto,
    GroupPostTaskResponseDto,
    GroupRecruitDetailResponseDto,
    GroupRecruitListItemResponseDto,
    GroupRecruitListResponseDto,
    GroupRegisterRequestDto,
    GroupRegisterResponseDto,
    GroupTaskCompleteAdminRequestDto,
    GroupTaskCompleteResponseDto,
    GroupTaskDetailResponseDto,
    GroupTaskResponseDto,
    GroupNotifyResponseDto,
    GroupApprovePeopleResponseDto,
)


router = APIRouter()

engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)
participant_service = ParticipantService(engine=engine)
Base.metadata.create_all(bind=engine)


@router.post("/group/register")
def register(req: GroupRegisterRequestDto) -> ApiResponse[GroupRegisterResponseDto]:
    return ApiResponse.ok(GroupRegisterResponseDto(id=1))


@router.post("/group/{room_id}/participate")
def participate(room_id: int) -> ApiResponse[GroupParticipateResponseDto]:
    return ApiResponse.ok(GroupParticipateResponseDto(id=1))


@router.post("/group/{group_id}/recruit")
def post_recruit(group_id: int, req: GroupPostRecruitRequestDto) -> ApiResponse[GroupPostRecruitResponseDto]:
    return ApiResponse.ok(GroupPostRecruitResponseDto(id=1))


@router.post("/group/{room_id}/task")
def post_task(room_id: int, req: GroupPostTaskRequestDto) -> ApiResponse[GroupPostTaskResponseDto]:
    return ApiResponse.ok(GroupPostTaskResponseDto(id=1))


@router.get("/groups/recruits")
def get_recruits() -> ApiResponse[GroupRecruitListResponseDto]:
    return ApiResponse.ok(
        GroupRecruitListResponseDto(
            recruits=[
                GroupRecruitListItemResponseDto(id=1, title="test", description="test", room_name="test"),
                GroupRecruitListItemResponseDto(id=1, title="test", description="test", room_name="test"),
                GroupRecruitListItemResponseDto(id=1, title="test", description="test", room_name="test"),
            ]
        )
    )


@router.get("/groups/recruits/search")
def get_recruits(query: str) -> ApiResponse[GroupRecruitListResponseDto]:
    return ApiResponse.ok(
        GroupRecruitListResponseDto(
            recruits=[
                GroupRecruitListItemResponseDto(id=1, title="test", description="test", room_name="test"),
                GroupRecruitListItemResponseDto(id=1, title="test", description="test", room_name="test"),
                GroupRecruitListItemResponseDto(id=1, title="test", description="test", room_name="test"),
            ]
        )
    )


@router.get("/group/{group_id}/recruit")
def get_recruit_detail(group_id: int) -> ApiResponse[GroupRecruitDetailResponseDto]:
    return ApiResponse.ok(
        GroupRecruitDetailResponseDto(
            id=1, title="test", room_name="test", admin_name="test", description="test", people=1, max_people=2
        )
    )


@router.get("/group/{group_id}/notice/{notice_id}")
def get_recruit_notice_detail(group_id: int, notice_id: int) -> ApiResponse[GroupNoticeDetailResponseDto]:
    return ApiResponse.ok(
        GroupNoticeDetailResponseDto(
            id=notice_id,
            title="test",
            description="test",
            comments=[
                GroupNoticeCommentResponseDto(author="test", text="test"),
                GroupNoticeCommentResponseDto(author="test", text="test"),
                GroupNoticeCommentResponseDto(author="test", text="test"),
            ],
        )
    )


@router.get("/group/{group_id}/task/{task_id}")
def get_recruit_notice_detail(group_id: int, task_id: int) -> ApiResponse[GroupTaskDetailResponseDto]:
    return ApiResponse.ok(
        GroupTaskDetailResponseDto(
            id=task_id,
            title="test",
            start_date="2023-01-01T00:00:00",
            end_date="2023-01-31T00:00:00",
            description="test",
            not_started=["p1", "p2"],
            comments=[
                GroupNoticeCommentResponseDto(author="test", text="test"),
                GroupNoticeCommentResponseDto(author="test", text="test"),
                GroupNoticeCommentResponseDto(author="test", text="test"),
            ],
        )
    )


@router.get("/group/{group_id}/task/{task_id}/notify")
def get_notify(group_id: int, task_id: int) -> ApiResponse[GroupNotifyResponseDto]:
    return ApiResponse.ok(
        GroupNotifyResponseDto(
            users=[
                GroupApprovePeopleResponseDto(id="1", nickname="nicknmae"),
                GroupApprovePeopleResponseDto(id="1", nickname="nicknmae"),
            ]
        )
    )


@router.post("/group/{group_id}/task/{task_id}/complete/user")
def complete_task_user(group_id: int, task_id: int) -> ApiResponse[GroupTaskCompleteResponseDto]:
    return ApiResponse.ok(GroupTaskCompleteResponseDto(id=task_id))


@router.post("/group/{group_id}/notice/{notice_id}/comment")
def comment_notice(
    group_id: int, notice_id: int, req: GroupCommentPostRequestDto
) -> ApiResponse[GroupCommentPostResponseDto]:
    return ApiResponse.ok(GroupCommentPostResponseDto(id=notice_id))


@router.post("/group/{group_id}/task/{task_id}/comment")
def comment_task(
    group_id: int, task_id: int, req: GroupCommentPostRequestDto
) -> ApiResponse[GroupCommentPostResponseDto]:
    return ApiResponse.ok(GroupCommentPostResponseDto(id=task_id))


@router.post("/group/{group_id}/notice")
def create_notice(group_id: int, req: GroupNoticePostRequestDto) -> ApiResponse[GroupNoticePostResponseDto]:
    return ApiResponse.ok(GroupNoticePostResponseDto(id=1))


@router.post("/group/{group_id}/task/{task_id}/complete/admin")
def complete_task_user(
    group_id: int, task_id: int, req: GroupTaskCompleteAdminRequestDto
) -> ApiResponse[GroupTaskCompleteResponseDto]:
    return ApiResponse.ok(GroupTaskCompleteResponseDto(id=task_id))


@router.get("/group/{group_id}")
def get_group_detail(group_id: int) -> ApiResponse[GroupDetailResponseDto]:
    res = GroupDetailResponseDto(
        name="test",
        admin=GroupAdminResponseDto(id="test-admin", nickname="test-nickname"),
        participants=[
            GroupParticipantResponseDto(id="test-participant1", nickname="test"),
            GroupParticipantResponseDto(id="test-participant2", nickname="test"),
        ],
        tasks=[
            GroupTaskResponseDto(
                id=1,
                title="test",
                start_date="2023-11-11T00:00:00",
                end_date="2023-11-12T00:00:00",
                not_started=["p1", "p2"],
            )
        ],
        notices=[GroupNoticeResponseDto(id=1, title="str", author_name="test-name")],
        description="...",
    )
    return ApiResponse.ok(res)
