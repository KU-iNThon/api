from fastapi import APIRouter, Response

from fastlib.view.model.api import ApiResponse
from fastlib.view.model.user import (
    UserLoginResponseDto,
    UserProfileResponseDto,
    UserProfileGroupResponseDto,
    UserProfileSummaryResponseDto,
    UserRegisterResponseDto,
    UserRegisterRequestDto
)



router = APIRouter()


@router.get("/user/login")
def login(id: str, pw: str, response: Response) -> ApiResponse[UserLoginResponseDto]:
    response.set_cookie("session_id", id)
    return ApiResponse.ok(UserLoginResponseDto(id=id, nickname="test", region="korea"))

@router.get("/user/{user_id}")
def profile(user_id: str) -> ApiResponse[UserProfileResponseDto]:
    res = UserProfileResponseDto(
        id=user_id,
        nickname="test",
        region="aa",
        groups=[
            UserProfileGroupResponseDto(id=1, name="test", total_task=2, completed_task=1, role="user", closed=False),
            UserProfileGroupResponseDto(id=2, name="test1", total_task=2, completed_task=1, role="admin", closed=False),
            UserProfileGroupResponseDto(id=2, name="test1", total_task=2, completed_task=1, role="user", closed=True),
            UserProfileGroupResponseDto(id=2, name="test1", total_task=2, completed_task=1, role="admin", closed=True),
        ],
        summary=UserProfileSummaryResponseDto(completed_task=2, total_task=10),
    )
    return ApiResponse.ok(res)

@router.post("/user/register")
def login(request: UserRegisterRequestDto) -> ApiResponse[UserRegisterResponseDto]:
    return ApiResponse.ok(UserRegisterResponseDto(id="test-id"))
