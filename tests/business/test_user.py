import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.business.model.user import UserRegisterRequestDto
from fastlib.business.user import UserBusiness
from fastlib.entity.user import User
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


def test_register(Session, user_service):
    business = UserBusiness(user_service=user_service, session=Session)
    req = UserRegisterRequestDto(
        id="test@com",
        nickname="test",
        pw="test",
        region="test-region",
    )
    res = business.register(req)
    assert res.id == req.id

    with Session() as session:
        e = session.query(User).filter_by(id=res.id).first()
        session.delete(e)
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
