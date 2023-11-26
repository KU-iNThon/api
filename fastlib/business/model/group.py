from datetime import datetime
from typing import List

from pydantic import BaseModel


class GroupRegisterRequestDto(BaseModel):
    name: str
    description: str


class GroupRegisterResponseDto(BaseModel):
    id: int


class GroupPostRecruitRequestDto(BaseModel):
    title: str
    description: str
    tags: List[str]


class GroupPostRecruitResponseDto(BaseModel):
    id: int


class GroupNoticePostRequestDto(BaseModel):
    title: str
    description: str


class GroupNoticePostResponseDto(BaseModel):
    id: int


class GroupParticipateResponseDto(BaseModel):
    id: int


class GroupPostTaskRequestDto(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime


class GroupPostTaskResponseDto(BaseModel):
    id: int
