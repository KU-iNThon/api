from pydantic import BaseModel


class GroupPostTaskRequestDto(BaseModel):
    title: str
    start_date: str
    end_date: str


class GroupPostTaskResponseDto(BaseModel):
    id: int
