from fastapi import HTTPException
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.user import User


class UserService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        User.metadata.create_all(engine)

    def login(self, session: Session, entity: User) -> User:
        res = session.query(User).filter_by(id=entity.id).first()
        if res is None:
            raise HTTPException(status_code=404, detail="로그인 정보를 찾을 수 없습니다.")
        else:
            return res

    def register(self, session: Session, entity: User) -> User:
        if session.query(User).filter_by(id=entity.id).first():
            raise HTTPException(status_code=409, detail="중복된 사용자입니다.")
        else:
            session.add(entity)
            res = session.query(User).filter_by(id=entity.id).first()
            session.commit()
            return res

    def find(self, session: Session, id_: str) -> User:
        if user := session.query(User).filter_by(id=id_).first():
            return user
        else:
            raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다.")
