from fastapi import HTTPException
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.user import User


class UserService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        self.__session = sessionmaker(bind=engine)
        User.metadata.create_all(engine)

    def login(self, user: User):
        with self.__session() as session:
            res = session.query(User).filter_by(id=user.id).first()
            if res is None:
                raise HTTPException(status_code=404, detail="로그인 정보를 찾을 수 없습니다.")
            else:
                return res
