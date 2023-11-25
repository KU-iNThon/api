import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.user import User
from tests.view.schema.user import UserLoginResponseSchema, UserProfileResponseSchema, UserRegisterResponseSchema


while "tests" not in os.listdir():
    os.chdir("..")


@pytest.fixture()
def engine():
    return create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)


@pytest.fixture()
def Session(engine):
    return sessionmaker(bind=engine)


def test_user_login(Session):
    from main import app

    # given
    client = TestClient(app)
    # when
    client.post("/user/register", json={"id": "test_id", "pw": "test-pw", "nickname": "test", "region": "region"})
    res = client.get("/user/login?id=test_id&pw=test-pw")
    # then
    assert res.status_code == 200
    body = res.json()["data"]
    assert UserLoginResponseSchema().validate(body) == {}
    set_cookies: str = res.headers["set-cookie"]
    assert set_cookies.find("session_id=test_id") != -1

    with Session() as session:
        e = session.query(User).filter_by(id=body["id"]).first()
        session.delete(e)
        session.commit()


def test_user_profile():
    from main import app

    # given
    client = TestClient(app)
    # when
    res = client.get("/user/1")
    # then
    assert res.status_code == 200
    body = res.json()["data"]
    assert UserProfileResponseSchema().validate(body) == {}


def test_user_register(Session):
    from main import app

    # given
    client = TestClient(app)
    res = client.post(
        "/user/register", json={"id": "test_id2", "pw": "test-pw", "nickname": "test", "region": "region"}
    )
    # then
    assert res.status_code == 200

    body = res.json()["data"]
    assert UserRegisterResponseSchema().validate(body) == {}

    with Session() as session:
        e = session.query(User).filter_by(id=body["id"]).first()
        session.delete(e)
        session.commit()
