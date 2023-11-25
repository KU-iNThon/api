from fastapi import APIRouter, Response

from fastlib.view.model.api import ApiResponse
from fastlib.view.model.user import UserLoginResponseDto


router = APIRouter()


@router.get("/user/login")
def login(id: str, pw: str, response: Response) -> ApiResponse[UserLoginResponseDto]:
    response.set_cookie("session_id", id)
    return ApiResponse.ok(UserLoginResponseDto(id=id, nickname="test", region="korea"))
