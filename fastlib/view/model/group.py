from pydantic import BaseModel


class GroupRegisterRequestDto(BaseModel):
    name: str
    description: str


class GroupRegisterResponseDto(BaseModel):
    id: int


class GroupParticipateResponseDto(BaseModel):
    id: int
