from fastapi import APIRouter

from fastlib.view.model.gorup import GroupRegisterRequestDto, GroupRegisterResponseDto


router = APIRouter()


@router.post("/group/register")
def register(req: GroupRegisterRequestDto) -> GroupRegisterResponseDto:
    return GroupRegisterResponseDto(id=1)
