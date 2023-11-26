from pydantic import BaseModel


class CommentRequestDto(BaseModel):
    text: str


class CommentResponseDto(BaseModel):
    id: int
