import os

import dotenv
from fastapi.testclient import TestClient

from tests.view.schema.user import UserLoginResponseSchema


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
