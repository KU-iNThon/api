# from sqlalchemy import Column, ForeignKey, Integer, VARCHAR
# from sqlalchemy.orm import declarative_base, relationship
#
# from fastlib.entity.base import Base
# from fastlib.entity.group import Group
# from fastlib.entity.participant import Participant
# from fastlib.entity.user import User
#
#
# def test_engine():
#     from sqlalchemy import create_engine
#     from sqlalchemy.orm import sessionmaker
#
#     engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/ku', echo=True)
#     Session = sessionmaker(bind=engine)
#
#     Base = declarative_base()
#
#
#     # Parent 모델 정의
#     class Parent(Base):
#         __tablename__ = 'parents'
#
#         id = Column(Integer, primary_key=True)
#         name = Column(VARCHAR(20))
#
#         # 1:N 관계 설정
#         children = relationship("Child", back_populates="parent")
#
#
#     # Child 모델 정의
#     class Child(Base):
#         __tablename__ = 'children'
#
#         id = Column(Integer, primary_key=True)
#         name = Column(VARCHAR(20))
#
#         # Parent의 id를 외래키로 설정
#         parent_id = Column(Integer, ForeignKey('parents.id'))
#
#         # Parent와의 관계 설정
#         parent = relationship("Parent", back_populates="children")
#
#
#     # 데이터베이스에 테이블을 생성
#     Base.metadata.create_all(engine)
#
#     # 데이터베이스에 세션을 만들고 데이터 추가
#     with Session() as session:
#         parent = Parent(name='Parent 1', children=[Child(name='Child 1'), Child(name='Child 2')])
#         session.add(parent)
#         session.commit()
#
#         # 쿼리를 사용하여 데이터 가져오기
#         loaded_parent = session.query(Parent).filter_by(name='Parent 1').first()
#         assert loaded_parent.name == parent.name
#         for child in loaded_parent.children:
#             assert child.name in {"Child 1", "Child 2"}
#
#
# def test_participant():
#     from sqlalchemy import create_engine
#     from sqlalchemy.orm import sessionmaker
#
#     engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/ku', echo=True)
#     Session = sessionmaker(bind=engine)
#     Base.metadata.create_all(engine)
#
#     with Session() as session:
#         user = User(id="test5", nickname='test', pw="test", region="test-region")
#         group = Group(name="test", description="test", max_people=10)
#         participant = Participant(user=user, group=group, role="admin")
#         session.add_all([user, group, participant])
#         session.commit()
#
#         assert user.id is not None and group.id is not None
#         assert participant.user_id == user.id
#         assert participant.group_id == group.id
