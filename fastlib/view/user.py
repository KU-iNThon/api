from fastapi import APIRouter, Response
from sqlalchemy.orm import sessionmaker

from fastlib.business.model.user import UserLoginResponseDto, UserRegisterRequestDto, UserRegisterResponseDto
from fastlib.business.user import UserBusiness
from fastlib.resource import get_engine
from fastlib.service.task import TaskService
from fastlib.service.user import UserService
from fastlib.view.model.api import ApiResponse
from fastlib.view.model.user import (
    UserProfileGroupResponseDto,
    UserProfileResponseDto,
    UserProfileSummaryResponseDto,
)


router = APIRouter()

engine = get_engine()
user_service = UserService(engine=engine)
task_service = TaskService(engine=engine)
user_business = UserBusiness(session=sessionmaker(bind=engine), user_service=user_service)


@router.get("/user/login")
def login(id: str, pw: str, response: Response) -> ApiResponse[UserLoginResponseDto]:
    res = user_business.login(id, pw)
    response.set_cookie("session_id", res.id)
    return ApiResponse.ok(res)


# TODO :
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
        credit=100,
    )
    return ApiResponse.ok(res)


@router.post("/user/register")
def register(request: UserRegisterRequestDto) -> ApiResponse[UserRegisterResponseDto]:
    res = user_business.register(request)
    return ApiResponse.ok(res)
