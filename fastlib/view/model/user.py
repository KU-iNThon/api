from pydantic import BaseModel


class UserLoginResponseDto(BaseModel):
    id: str
    nickname: str
    region: str
