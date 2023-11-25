import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastlib.entity.participant import Participant
from fastlib.service.participant import ParticipantService


@pytest.fixture()
def engine():
    return create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)


@pytest.fixture()
def session(engine):
    return sessionmaker(bind=engine)()


def test_participant(session, engine):
    service = ParticipantService(engine=engine)
    entity1 = Participant(user_id=1, group_id=2)
    entity2 = Participant(user_id=1, group_id=2)
    res = service.participant(session=session, entity=entity1)
    with pytest.raises(HTTPException) as e:
        res = service.participant(session=session, entity=entity2)
    assert e.value.status_code == 404

    session.delete(res)
    session.commit()
