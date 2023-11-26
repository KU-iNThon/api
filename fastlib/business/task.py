from sqlalchemy.orm import sessionmaker

from fastlib.entity.task import Task
from fastlib.service.task import TaskService
from fastlib.business.model import GroupPostTaskRequestDto, GroupPostTaskResponseDto


class TaskBusiness:
    def __init__(self, session: sessionmaker, task_service: TaskService):
        self.__session = session
        self.__task_service = task_service

    def create(self, req: GroupPostTaskRequestDto) -> GroupPostTaskResponseDto:
        with self.__session() as session:
            task = Task(title=req.title, start_date=req.start_date, end_date=req.end_date)
            self.__task_service.save(session, task)
            res = GroupPostTaskResponseDto(id=task.id)
            return res
