from fastapi import APIRouter

from fastlib.view.model.api import ApiResponse
from fastlib.view.model.gorup import GroupRegisterRequestDto, GroupRegisterResponseDto


router = APIRouter()


@router.post("/group/register")
def register(req: GroupRegisterRequestDto) -> ApiResponse[GroupRegisterResponseDto]:
    return ApiResponse.ok(GroupRegisterResponseDto(id=1))
