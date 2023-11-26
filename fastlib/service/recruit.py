from fastapi import HTTPException
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.group import Group
from fastlib.entity.recruit import Recruit


class RecruitService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        Group.metadata.create_all(engine)

    def save(self, session: Session, entity: Recruit) -> Recruit:
        if session.query(Recruit).filter_by(group=entity.group).first():
            raise HTTPException(status_code=409, detail="이미 모집 공고가 등록되었습니다.")
        session.add(entity)
        return entity
