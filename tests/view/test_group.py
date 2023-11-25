import os

from fastapi.testclient import TestClient

from tests.view.schema.group import (
    GroupPostRecruitResponseSchema,
    GroupRecruitListResponseSchema,
    GroupRegisterResponseSchema,
)


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


def test_group_post_recruit():
    from main import app

    client = TestClient(app)
    res = client.post(
        "/group/1/recruit", json={"title": "test-title", "description": "description", "tags": ["tag-a", "tag-b"]}
    )
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupPostRecruitResponseSchema().validate(body) == {}


def test_group_recruit_list():
    from main import app

    client = TestClient(app)
    res = client.get("/groups/recruits")
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupRecruitListResponseSchema().validate(body) == {}
