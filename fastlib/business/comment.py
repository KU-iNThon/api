from sqlalchemy.orm import sessionmaker

from fastlib.business.model.comment import CommentRequestDto, CommentResponseDto

from fastlib.entity.comment import Comment
from fastlib.service.comment import CommentService


class CommentBusiness:
    def __init__(
        self,
        session: sessionmaker,
        comment_service: CommentService,
    ):
        self.__session = session
        self.__comment_service = comment_service

    def comment_task(self, user_id: str, group_id: int, task_id: int, req: CommentRequestDto) -> CommentResponseDto:
        with self.__session() as session:
            comment = Comment(user_id=user_id, group_id=group_id, task_id=task_id, text=req.text)
            self.__comment_service.save(session, comment)
            res = CommentResponseDto(id=comment.id)
        return res

    def comment_notice(self, user_id: str, group_id: int, notice_id: int, req: CommentRequestDto) -> CommentResponseDto:
        with self.__session() as session:
            comment = Comment(user_id=user_id, group_id=group_id, notice_id=notice_id, text=req.text)
            self.__comment_service.save(session, comment)
            res = CommentResponseDto(id=comment.id)
        return res
