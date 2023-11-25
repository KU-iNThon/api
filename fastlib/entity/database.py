from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base


class User(Base):
    __tablename__ = "users"
    id = Column(VARCHAR(20), primary_key=True, index=True)
    nickname = Column(VARCHAR(30))
    pw = Column(VARCHAR(30))
    region = Column(VARCHAR(50))

    participants = relationship("Participant", back_populates="user")
    notices = relationship("Notice", back_populates="user")
    participants_tasks = relationship("Participants_task", back_populates="user")
    comments = relationship("Comment", back_populates="user")


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(20))
    description = Column(String)
    max_people = Column(Integer)

    participants = relationship("Participant", back_populates="group")
    notices = relationship("Notice", back_populates="group")
    tasks = relationship("Task", back_populates="group")
    participants_tasks = relationship("Participants_task", back_populates="group")
    comments = relationship("Comment", back_populates="group")


class Participant(Base):
    __tablename__ = "participants"
    user_id = Column(VARCHAR(20), ForeignKey("user.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    role = Column(VARCHAR(10))

    user = relationship("User", back_populates="participants")
    group = relationship("Group", back_populates="participants")


class Notice(Base):
    __tablename__ = "notices"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    user_id = Column(VARCHAR(20), ForeignKey=("users.id"))
    title = Column(VARCHAR(50))
    description = Column(String)

    group = relationship("Group", back_populates="notices")
    user = relationship("User", back_populates="notices")
    comments = relationship("Comment", back_populates="notice")


class Task_status(Base):
    __tablename__ = "task_status"
    id = Column(Integer, primary_key=True, index=True)
    participants_tasks = relationship("Participants_task", back_populates="status")


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    title = Column(VARCHAR(20))
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    group = relationship("Group", back_populates="tasks")
    participants_tasks = relationship("Participants_task", back_populates="task")
    comments = relationship("Comment", back_populates="task")


class Participant_task(Base):
    __tablename__ = "participant_tasks"
    task_id = Column(Integer, ForeignKey=("tasks.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    user_id = Column(VARCHAR(20), ForeignKey("user.id"))
    status_id = Column(VARCHAR(20), ForeignKey("task_status.id"))

    task = relationship("Task", back_populates="participant_tasks")
    group = relationship("Group", back_populates="participant_tasks")
    user = relationship("User", back_populates="participant_tasks")
    status = relationship("Task_status", back_populates="task_status")


class Comment(Base):
    __tablename__ = "commnents"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column((VARCHAR(20)), ForeignKey("users.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
    notice_id = Column(Integer, ForeignKey("notices.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    text = Column(String)
    wroten_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="comments")
    group = relationship("Group", back_populates="comments")
    notice = relationship("Notice", back_populates="commnets")
    task = relationship("Task", back_populates="comments")
