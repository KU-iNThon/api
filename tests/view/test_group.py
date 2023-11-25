import os

from fastapi.testclient import TestClient

from tests.view.schema.group import (
    GroupNoticeDetailResponseSchema,
    GroupPostRecruitResponseSchema,
    GroupRecruitDetailResponseSchema,
    GroupRecruitListResponseSchema,
    GroupRegisterResponseSchema,
    GroupTaskDetailResponseSchema,
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


def test_group_recruit_search():
    from main import app

    client = TestClient(app)
    res = client.get("/groups/recruits/search?query=test")
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupRecruitListResponseSchema().validate(body) == {}


def test_group_recruit_detail():
    from main import app

    client = TestClient(app)
    res = client.get("/group/1/recruit")
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupRecruitDetailResponseSchema().validate(body) == {}


def test_group_notice_detail():
    from main import app

    client = TestClient(app)
    res = client.get("/group/1/notice/1")
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupNoticeDetailResponseSchema().validate(body) == {}


def test_group_task_detail():
    from main import app

    client = TestClient(app)
    res = client.get("/group/1/task/1")
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupTaskDetailResponseSchema().validate(body) == {}
