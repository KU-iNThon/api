from fastapi import HTTPException
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.group import Group


class GroupService:
    def __init__(self, engine: Engine):
        self.__engine = engine

    def save(self, session: Session, entity: Group) -> Group:
        session.add(entity)
        session.commit()
        return entity

    def find(self, session: Session, id_: int) -> Group:
        if group := session.query(Group).filter_by(id=id_).first():
            return group
        else:
            raise HTTPException(status_code=404, detail="그룹을 찾을 수 없습니다.")
