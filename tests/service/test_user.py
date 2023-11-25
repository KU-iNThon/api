import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine

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
