from typing import List

from pydantic import BaseModel


class GroupRegisterRequestDto(BaseModel):
    name: str
    description: str


class GroupRegisterResponseDto(BaseModel):
    id: int


class GroupParticipateResponseDto(BaseModel):
    id: int


class GroupPostRecruitRequestDto(BaseModel):
    title: str
    description: str
    tags: List[str]


class GroupPostRecruitResponseDto(BaseModel):
    id: int


class GroupPostTaskRequestDto(BaseModel):
    title: str
    start_date: str
    end_date: str


class GroupPostTaskResponseDto(BaseModel):
    id: int


class GroupRecruitListItemResponseDto(BaseModel):
    id: int
    title: str
    description: str
    room_name: str


class GroupRecruitListResponseDto(BaseModel):
    recruits: List[GroupRecruitListItemResponseDto]


class GroupRecruitDetailResponseDto(BaseModel):
    title: str
    id: int
    room_name: str
    admin_name: str
    description: str
    people: int
    max_people: int


class GroupNoticeCommentResponseDto(BaseModel):
    author: str
    text: str


class GroupNoticeDetailResponseDto(BaseModel):
    id: int
    title: str
    description: str
    comments: List[GroupNoticeCommentResponseDto]


class GroupTaskDetailResponseDto(BaseModel):
    id: int
    title: str
    start_date: str
    end_date: str
    not_started: List[str]
    comments: List[GroupNoticeCommentResponseDto]


class GroupTaskCompleteResponseDto(BaseModel):
    id: int


class GroupCommentPostRequestDto(BaseModel):
    text: str


class GroupCommentPostResponseDto(BaseModel):
    id: int
