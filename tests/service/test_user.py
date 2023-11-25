import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.user import User
from fastlib.service.user import UserService


@pytest.fixture()
def engine():
    return create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)


def test_login(engine):
    service = UserService(engine=engine)
    entity = User(nickname="test", id="invalid@com", pw="test-pw")
    with pytest.raises(HTTPException) as e:
        res = service.login(entity)
    assert e.value.status_code == 404


def test_register_ok(engine):
    service = UserService(engine=engine)
    entity = User(nickname="test1", id="new10@com", pw="test-pw")
    res = service.register(entity)
    # clean
    with sessionmaker(bind=engine)() as session:
        session.add_all([res, entity])
        assert res.id == entity.id
        session.delete(res)
        session.delete(entity)
        session.commit()


def test_register_duplicated(engine):
    service = UserService(engine=engine)
    entity1 = User(nickname="test2", id="new3@com", pw="test-pw")
    entity2 = User(nickname="test2", id="new3@com", pw="test-pw")
    res = service.register(entity1)
    with pytest.raises(HTTPException) as e:
        service.register(entity2)
    assert e.value.status_code == 409

    with sessionmaker(bind=engine)() as session:
        session.add(res)
        session.delete(res)
        session.commit()
