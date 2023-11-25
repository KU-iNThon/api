from sqlalchemy.orm import sessionmaker

from fastlib.business.model.user import UserRegisterRequestDto, UserRegisterResponseDto
from fastlib.entity.user import User
from fastlib.service.user import UserService


class UserBusiness:
    def __init__(self, session: sessionmaker, user_service: UserService):
        self.__session = session
        self.__user_service = user_service

    def register(self, req: UserRegisterRequestDto) -> UserRegisterResponseDto:
        with self.__session() as session:
            entity = User(id=req.id, nickname=req.nickname, pw=req.pw, region=req.region)
            result = self.__user_service.register(session=session, entity=entity)
            res = UserRegisterResponseDto(id=result.id)
            session.commit()
        return res
