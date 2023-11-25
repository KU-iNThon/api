from fastapi import APIRouter

from fastlib.view.model.api import ApiResponse
from fastlib.view.model.group import (
    GroupRegisterRequestDto,
    GroupRegisterResponseDto,
    GroupParticipateResponseDto,
    GroupPostRecruitRequestDto,
    GroupPostRecruitResponseDto,
    GroupRegisterRequestDto,
    GroupRegisterResponseDto,
    GroupPostTaskRequestDto,
    GroupPostTaskResponseDto,
)


router = APIRouter()


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
