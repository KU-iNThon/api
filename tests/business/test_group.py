import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.business.group import GroupBusiness
from fastlib.business.model.group import GroupPostRecruitRequestDto, GroupRegisterRequestDto
from fastlib.entity.group import Group
from fastlib.entity.participant import Participant
from fastlib.entity.recruit import Recruit
from fastlib.entity.user import User
from fastlib.service.group import GroupService
from fastlib.service.participant import ParticipantService
from fastlib.service.recruit import RecruitService
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


@pytest.fixture
def recruit_service(engine):
    return RecruitService(engine)


@pytest.fixture
def business(Session, user_service, participant_service, group_service, recruit_service):
    return GroupBusiness(
        session=Session,
        user_service=user_service,
        participant_service=participant_service,
        group_service=group_service,
        recruit_service=recruit_service,
    )


def test_create(business, Session, user_service, participant_service, group_service):
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


def test_create_recruit(Session, business, user_service, group_service):
    user = User(id="test@com", nickname="test", pw="test", region="test")

    with Session() as session:
        user = user_service.register(session=session, entity=user)
        session.commit()
        user_id = user.id
    group = business.create(
        user_id=user_id,
        req=GroupRegisterRequestDto(
            name="test",
            description="test",
        ),
    )
    req = GroupPostRecruitRequestDto(title="test", description="test", tags=["a", "b", "c"])
    recruit = business.create_recruit(user_id=user_id, group_id=group.id, req=req)

    assert recruit.id == group.id
    with Session() as session:
        g = session.query(Group).filter_by(id=group.id).first()
        for p in g.participants:
            session.delete(p)
        session.commit()
        r = session.query(Recruit).filter_by(id=recruit.id).first()
        session.delete(r)
        session.delete(g)
        session.delete(user)
        session.commit()
