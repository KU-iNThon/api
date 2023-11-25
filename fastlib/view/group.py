from fastapi import APIRouter

from fastlib.view.model.api import ApiResponse
from fastlib.view.model.gorup import (
    GroupPostRecruitRequestDto,
    GroupPostRecruitResponseDto,
    GroupRegisterRequestDto,
    GroupRegisterResponseDto,
)


router = APIRouter()


@router.post("/group/register")
def register(req: GroupRegisterRequestDto) -> ApiResponse[GroupRegisterResponseDto]:
    return ApiResponse.ok(GroupRegisterResponseDto(id=1))


@router.post("/group/{group_id}/recruit")
def post_recruit(req: GroupPostRecruitRequestDto) -> ApiResponse[GroupPostRecruitResponseDto]:
    return ApiResponse.ok(GroupPostRecruitResponseDto(id=1))
