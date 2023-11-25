from fastapi import APIRouter

from fastlib.view.model.api import ApiResponse
from fastlib.view.model.group import (
    GroupParticipateResponseDto,
    GroupPostRecruitRequestDto,
    GroupPostRecruitResponseDto,
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
