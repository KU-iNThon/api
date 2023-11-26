import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.group import Group
from fastlib.service.group import GroupService


@pytest.fixture()
def engine():
    return create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)


@pytest.fixture()
def session(engine):
    return sessionmaker(bind=engine)()


def test_make_group(engine, session):
    service = GroupService(engine=engine)

    entity = Group(name="test", description="test", max_people=10)

    res = service.save(session=session, entity=entity)

    assert res.id is not None

    session.delete(res)
    session.commit()
