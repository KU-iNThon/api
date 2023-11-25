from pydantic import BaseModel
from typing import List


class UserLoginResponseDto(BaseModel):
    id: str
    nickname: str
    region: str

class UserProfileSummaryResponseDto(BaseModel):
    completed_task: int
    total_task: int


class UserProfileGroupResponseDto(BaseModel):
    id: int
    name: str
    total_task: int
    completed_task: int
    role: str
    closed: bool


class UserProfileResponseDto(BaseModel):
    id: str
    nickname: str
    region: str
    groups: list[UserProfileGroupResponseDto]
    summary: UserProfileSummaryResponseDto

class UserRegisterRequestDto(BaseModel):
    id: str
    pw: str
    nickname: str
    region: str


class UserRegisterResponseDto(BaseModel):
    id: str

