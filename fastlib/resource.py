from sqlalchemy import create_engine


__engine = None


def get_engine():
    global __engine
    if __engine is None:
        __engine = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/ku", echo=True)
    return __engine
