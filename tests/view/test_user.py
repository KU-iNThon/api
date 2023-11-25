import os

from fastapi.testclient import TestClient

from tests.view.schema.user import UserLoginResponseSchema, UserProfileResponseSchema, UserRegisterResponseSchema


while "tests" not in os.listdir():
    os.chdir("..")


def test_user_login():
    from main import app

    # given
    client = TestClient(app)
    # when
    res = client.get("/user/login?id=test-id&pw=test-pw")
    # then
    assert res.status_code == 200
    body = res.json()["data"]
    assert UserLoginResponseSchema().validate(body) == {}
    set_cookies: str = res.headers["set-cookie"]
    assert set_cookies.find("session_id=test-id") != -1

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

def test_user_register():
    from main import app
    
    # given
    client = TestClient(app)
    res = client.post("/user/register", json={"id": "test_id", "pw": "test-pw", "nickname": "test", "region": "region"})
    # then
    assert res.status_code == 200

    body = res.json()["data"]
    assert UserRegisterResponseSchema().validate(body) == {}
