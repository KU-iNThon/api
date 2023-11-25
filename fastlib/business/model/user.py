from pydantic import BaseModel


class UserRegisterRequestDto(BaseModel):
    id: str
    pw: str
    nickname: str
    region: str


class UserRegisterResponseDto(BaseModel):
    id: str


class UserLoginResponseDto(BaseModel):
    id: str
    nickname: str
    region: str
