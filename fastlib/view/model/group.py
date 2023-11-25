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
