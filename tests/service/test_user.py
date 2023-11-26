import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.user import User
from fastlib.service.user import UserService


@pytest.fixture()
def engine():
    return create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)

@pytest.fixture
def session(engine):
    return sessionmaker(bind=engine)()


def test_login(session, engine):
    service = UserService(engine=engine)
    entity = User(nickname="test", id="invalid@com", pw="test-pw")
    with pytest.raises(HTTPException) as e:
        res = service.login(session=session, entity=entity)
    assert e.value.status_code == 404


def test_register_ok(session, engine):
    service = UserService(engine=engine)
    entity = User(nickname="test1", id="new10@com", pw="test-pw", region="test")
    res = service.register(session=session, entity=entity)
    # clean
    assert res.id == entity.id
    session.delete(res)
    session.commit()


def test_register_duplicated(session, engine):
    service = UserService(engine=engine)
    entity1 = User(nickname="test2", id="new3@com", pw="test-pw", region="test")
    entity2 = User(nickname="test2", id="new3@com", pw="test-pw", region="test")
    res = service.register(session=session, entity=entity1)
    with pytest.raises(HTTPException) as e:
        service.register(session=session, entity=entity2)
    assert e.value.status_code == 409

    session.delete(res)
    session.commit()
