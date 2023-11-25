from fastapi import APIRouter

from fastlib.view.model.api import ApiResponse
from fastlib.view.model.group import (
    GroupParticipateResponseDto,
    GroupPostRecruitRequestDto,
    GroupPostRecruitResponseDto,
    GroupRecruitDetailResponseDto,
    GroupRecruitListItemResponseDto,
    GroupRecruitListResponseDto,
    GroupRegisterRequestDto,
    GroupRegisterResponseDto,
)


router = APIRouter()


@router.post("/group/register")
def register(req: GroupRegisterRequestDto) -> ApiResponse[GroupRegisterResponseDto]:
    return ApiResponse.ok(GroupRegisterResponseDto(id=1))


@router.post("/group/{room_id}/participate")
def participate(room_id: int) -> GroupParticipateResponseDto:
    return ApiResponse.ok(GroupParticipateResponseDto(id=1))


@router.post("/group/{group_id}/recruit")
def post_recruit(req: GroupPostRecruitRequestDto) -> ApiResponse[GroupPostRecruitResponseDto]:
    return ApiResponse.ok(GroupPostRecruitResponseDto(id=1))


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
