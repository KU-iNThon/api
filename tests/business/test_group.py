import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.business.group import GroupBusiness
from fastlib.business.model.group import GroupRegisterRequestDto
from fastlib.business.model.user import UserRegisterRequestDto
from fastlib.business.user import UserBusiness
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
def Session(engine):
    return sessionmaker(bind=engine)


@pytest.fixture
def user_service(engine):
    return UserService(engine)


@pytest.fixture
def participant_service(engine):
    return ParticipantService(engine)


@pytest.fixture
def group_service(engine):
    return GroupService(engine)


def test_create(Session, user_service, participant_service, group_service):
    business = GroupBusiness(
        user_service=user_service, session=Session, participant_service=participant_service, group_service=group_service
    )
    req = GroupRegisterRequestDto(name="test", description="test")

    user = User(id="test@com", nickname="test", pw="test", region="test")
    with Session() as session:
        user_service.register(session, user)

    res = business.create(req=req, user_id="test@com")

    with Session() as session:
        p = session.query(Participant).filter_by(user_id="test@com", group_id=res.id).first()
        e = session.query(User).filter_by(id="test@com").first()
        g = session.query(Group).filter_by(id=res.id).first()
        session.delete(e)
        session.delete(p)
        session.delete(g)
        session.commit()


def test_login(Session, user_service):
    business = UserBusiness(user_service=user_service, session=Session)
    req = UserRegisterRequestDto(
        id="test@com",
        nickname="test",
        pw="test",
        region="test-region",
    )
    business.register(req)
    res = business.login(req.id, req.pw)
    assert res.id == req.id

    with Session() as session:
        e = session.query(User).filter_by(id=res.id).first()
        session.delete(e)
        session.commit()
