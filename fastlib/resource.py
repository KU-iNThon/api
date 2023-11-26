import os

from sqlalchemy import create_engine


__engine = None


def get_engine():
    global __engine
    if __engine is None:
        host = os.getenv("DB_HOST") or "127.0.0.1"
        __engine = create_engine(f"mysql+pymysql://root:1234@{host}/ku", echo=True)
    return __engine
