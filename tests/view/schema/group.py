from typing import List

from marshmallow import Schema, fields


class GroupRegisterResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class GroupPostRecruitResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class GroupParticipateResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class GroupPostTaskResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class _GroupRecruitListResponseSchema(Schema):
    id: int = fields.Integer(required=True)
    title: str = fields.String(required=True)
    description: str = fields.String(required=True)
    room_name: str = fields.String(required=True)


class GroupRecruitListResponseSchema(Schema):
    recruits: List[_GroupRecruitListResponseSchema] = fields.Nested(
        _GroupRecruitListResponseSchema, many=True, required=True
    )


class GroupRecruitDetailResponseSchema(Schema):
    id: int = fields.Integer(required=True)
    title: str = fields.String(required=True)
    room_name: str = fields.String(required=True)
    admin_name: str = fields.String(required=True)
    description: str = fields.String(required=True)
    people: int = fields.Integer(required=True)
    max_people: int = fields.Integer(required=True)


class GroupCommentResponseSchema(Schema):
    author: str = fields.String(required=True)
    text: str = fields.String(required=True)


class GroupNoticeDetailResponseSchema(Schema):
    id: int = fields.Integer(required=True)
    title: str = fields.String(required=True)
    description: str = fields.String(required=True)
    comments: List[GroupCommentResponseSchema] = fields.Nested(GroupCommentResponseSchema, many=True, required=True)


class GroupTaskDetailResponseSchema(Schema):
    id: int = fields.Integer(required=True)
    title: str = fields.String(required=True)
    start_date: str = fields.DateTime(required=True, format="iso")
    end_date: str = fields.DateTime(required=True, format="iso")
    not_started: List[str] = fields.List(fields.String(), required=True)
    comments: List[GroupCommentResponseSchema] = fields.Nested(GroupCommentResponseSchema, required=True, many=True)


class GroupTaskCompletedResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class GroupCommentPostResponseSchema(Schema):
    id: int = fields.Integer(required=True)
