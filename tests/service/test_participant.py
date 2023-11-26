import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.group import Group
from fastlib.entity.participant import Participant
from fastlib.entity.user import User
from fastlib.service.group import GroupService
from fastlib.service.participant import ParticipantService
from fastlib.service.user import UserService


@pytest.fixture()
def engine():
    return create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)


@pytest.fixture()
def session(engine):
    return sessionmaker(bind=engine)()


def test_participant(session, engine):
    service = ParticipantService(engine=engine)
    user_service = UserService(engine=engine)
    group_service = GroupService(engine=engine)
    user = User(id="test@com", nickname="test", pw="test", region="test")
    group = Group(name="test", description="test", max_people=3)
    user_service.register(session, user)
    group_service.save(session, group)

    participant = Participant(user=user, group=group, role="admin")
    service.save(session=session, entity=participant)

    assert participant.user_id == user.id
    assert participant.group_id == group.id

    session.delete(participant)
    session.delete(group)
    session.delete(user)
