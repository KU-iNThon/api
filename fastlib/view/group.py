from fastapi import APIRouter

from fastlib.view.model.api import ApiResponse
from fastlib.view.model.group import (
    GroupRegisterRequestDto,
    GroupRegisterResponseDto,
    GroupParticipateResponseDto,
)


router = APIRouter()


@router.post("/group/register")
def register(req: GroupRegisterRequestDto) -> GroupRegisterResponseDto:
    return GroupRegisterResponseDto(id=1)


@router.post("/group/{room_id}/participate")
def participate(room_id: int) -> GroupParticipateResponseDto:
    return ApiResponse.ok(GroupParticipateResponseDto(id=1))
