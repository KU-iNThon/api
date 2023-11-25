import os

from fastapi.testclient import TestClient

from tests.view.schema.group import GroupRegisterResponseSchema
from tests.view.schema.user import UserLoginResponseSchema


while "tests" not in os.listdir():
    os.chdir("..")


def test_group_register():
    from main import app

    # given
    client = TestClient(app)
    # when
    res = client.post("/group/register", json={"name": "test", "description": "test"})
    # then
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupRegisterResponseSchema().validate(body) == {}
