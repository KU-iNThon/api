import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.group import Group
from fastlib.entity.user import User
from tests.view.schema.group import (
    GroupCommentPostResponseSchema,
    GroupDetailResponseSchema,
    GroupNoticeDetailResponseSchema,
    GroupNoticePostResponseSchema,
    GroupNotifyResponseSchema,
    GroupParticipateResponseSchema,
    GroupPostRecruitResponseSchema,
    GroupPostTaskResponseSchema,
    GroupRecruitDetailResponseSchema,
    GroupRecruitListResponseSchema,
    GroupRegisterResponseSchema,
    GroupTaskCompletedResponseSchema,
    GroupTaskDetailResponseSchema,
)


while "tests" not in os.listdir():
    os.chdir("..")


@pytest.fixture()
def engine():
    return create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)


@pytest.fixture()
def Session(engine):
    return sessionmaker(bind=engine)


def test_group_register(Session):
    from main import app

    # given
    client = TestClient(app)
    # when
    client.post("/user/register", json={"id": "test@com", "pw": "test", "nickname": "test", "region": "seoul"})
    res = client.post(
        "/group/register", json={"name": "test", "description": "test"}, cookies={"session_id": "test@com"}
    )
    # then
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupRegisterResponseSchema().validate(body) == {}

    with Session() as session:
        g = session.query(Group).filter_by(id=body["id"]).first()
        for p in g.participants:
            session.delete(p)
        session.delete(g)
        u = session.query(User).filter_by(id="test@com").first()
        session.delete(u)
        session.commit()


def test_group_post_recruit(Session):
    from main import app

    client = TestClient(app)
    user = client.post(
        "/user/register", json={"id": "test@com", "pw": "test", "nickname": "test", "region": "seoul"}
    ).json()["data"]
    group = client.post(
        "/group/register", json={"name": "test", "description": "test"}, cookies={"session_id": "test@com"}
    ).json()["data"]

    res = client.post(
        f"/group/{group['id']}/recruit",
        json={"title": "test-title", "description": "description", "tags": ["tag-a", "tag-b"]},
        cookies={"session_id": user["id"]},
    )
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupPostRecruitResponseSchema().validate(body) == {}

    with Session() as session:
        user = session.query(User).filter_by(id=user["id"]).first()
        group = session.query(Group).filter_by(id=group["id"]).first()
        session.delete(group.recruit)
        session.commit()
        for p in group.participants:
            session.delete(p)
        session.commit()
        session.delete(group)
        session.delete(user)
        session.commit()


def test_group_participate(Session):
    from main import app

    client = TestClient(app)
    admin = client.post(
        "/user/register", json={"id": "test@com", "pw": "test", "nickname": "test", "region": "seoul"}
    ).json()["data"]
    user = client.post(
        "/user/register", json={"id": "user@com", "pw": "test", "nickname": "test", "region": "seoul"}
    ).json()["data"]
    group = client.post(
        "/group/register", json={"name": "test", "description": "test"}, cookies={"session_id": "test@com"}
    ).json()["data"]
    res = client.post(f"/group/{group['id']}/participate", cookies={"session_id": user["id"]})
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupParticipateResponseSchema().validate(body) == {}

    with Session() as session:
        a = session.query(User).filter_by(id=admin["id"]).first()
        u = session.query(User).filter_by(id=user["id"]).first()
        g = session.query(Group).filter_by(id=group["id"]).first()
        for p in g.participants:
            session.delete(p)
        session.commit()
        session.delete(g)
        session.delete(u)
        session.delete(a)
        session.commit()


def test_post_task(Session):
    from main import app

    client = TestClient(app)
    admin = client.post(
        "/user/register", json={"id": "test@com", "pw": "test", "nickname": "test", "region": "seoul"}
    ).json()["data"]
    group = client.post(
        "/group/register", json={"name": "test", "description": "test"}, cookies={"session_id": admin["id"]}
    ).json()["data"]
    res = client.post(
        f"/group/{group['id']}/task",
        json={"title": "test_title", "start_date": "2022-12-12T00:00:00", "end_date": "2022-12-12T00:00:00"},
        cookies={"session_id": admin["id"]},
    )

    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupPostTaskResponseSchema().validate(body) == {}

    with Session() as session:
        a = session.query(User).filter_by(id=admin["id"]).first()
        g = session.query(Group).filter_by(id=group["id"]).first()
        for t in g.tasks:
            session.delete(t)
        session.commit()
        for p in g.participants:
            session.delete(p)
        session.commit()
        session.delete(a)
        session.delete(g)
        session.commit()


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


def test_group_task_notify():
    from main import app

    client = TestClient(app)
    res = client.get("/group/1/task/1/notify")
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupNotifyResponseSchema().validate(body) == {}


def test_group_task_complete_user():
    from main import app

    client = TestClient(app)
    task_id = 4
    res = client.post(f"/group/1/task/{task_id}/complete/user")
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupTaskCompletedResponseSchema().validate(body) == {}
    assert task_id == body["id"]


def test_group_task_comment_post():
    from main import app

    client = TestClient(app)
    task_id = 4
    res = client.post(f"/group/1/task/{task_id}/comment", json={"text": "test-comment"})
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupCommentPostResponseSchema().validate(body) == {}
    assert task_id == body["id"]


def test_group_notice_comment_post():
    from main import app

    client = TestClient(app)
    notice_id = 4
    res = client.post(f"/group/1/notice/{notice_id}/comment", json={"text": "test-comment"})
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupCommentPostResponseSchema().validate(body) == {}
    assert notice_id == body["id"]


def test_group_notice_post(Session):
    from main import app

    client = TestClient(app)
    user = client.post(
        "/user/register", json={"id": "test@com", "pw": "test", "nickname": "test", "region": "seoul"}
    ).json()["data"]
    group = client.post(
        "/group/register", json={"name": "test", "description": "test"}, cookies={"session_id": "test@com"}
    ).json()["data"]

    res = client.post(
        f"/group/{group['id']}/notice",
        json={"title": "title", "description": "description"},
        cookies={"session_id": user["id"]},
    )
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupNoticePostResponseSchema().validate(body) == {}

    with Session() as session:
        user = session.query(User).filter_by(id=user["id"]).first()
        group = session.query(Group).filter_by(id=group["id"]).first()
        for n in group.notices:
            session.delete(n)
        session.commit()
        for p in group.participants:
            session.delete(p)
        session.commit()
        session.delete(group)
        session.delete(user)
        session.commit()


def test_group_task_complete_admin():
    from main import app

    client = TestClient(app)
    task_id = 4
    res = client.post(f"/group/1/task/{task_id}/complete/admin", json={"participant_id": 1})
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupTaskCompletedResponseSchema().validate(body) == {}
    assert task_id == body["id"]


def test_group_detail():
    from main import app

    client = TestClient(app)
    res = client.get("/group/1")
    assert res.status_code == 200
    body = res.json()["data"]
    assert GroupDetailResponseSchema().validate(body) == {}
