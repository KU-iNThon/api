from fastapi import HTTPException
from sqlalchemy import Engine
from sqlalchemy.orm import Session

from fastlib.entity.group import Group
from fastlib.entity.participant import Participant
from fastlib.entity.user import User


class ParticipantService:
    def __init__(self, engine: Engine):
        self.__engine = engine
        User.metadata.create_all(engine)
        Group.metadata.create_all(engine)
        Participant.metadata.create_all(engine)
