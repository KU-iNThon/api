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
    tags: List[str]


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


class GroupApprovePeopleResponseDto(BaseModel):
    id: int
    nickname: str


class GroupNotifyResponseDto(BaseModel):
    users: List[GroupApprovePeopleResponseDto]


class GroupTaskCompleteResponseDto(BaseModel):
    id: int


class GroupCommentPostRequestDto(BaseModel):
    text: str


class GroupCommentPostResponseDto(BaseModel):
    id: int


class GroupNoticePostRequestDto(BaseModel):
    title: str
    description: str


class GroupNoticePostResponseDto(BaseModel):
    id: int


class GroupTaskCompleteAdminRequestDto(BaseModel):
    participant_id: int


class GroupAdminResponseDto(BaseModel):
    id: str
    nickname: str


class GroupParticipantResponseDto(BaseModel):
    id: str
    nickname: str


class GroupTaskResponseDto(BaseModel):
    id: int
    title: str
    start_date: str
    end_date: str
    not_started: List[str]


class GroupNoticeResponseDto(BaseModel):
    id: int
    title: str
    author_name: str


class GroupDetailResponseDto(BaseModel):
    name: str
    admin: GroupAdminResponseDto
    participants: List[GroupParticipantResponseDto]
    tasks: List[GroupTaskResponseDto]
    notices: List[GroupNoticeResponseDto]
    description: str
