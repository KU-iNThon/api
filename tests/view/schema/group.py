from typing import List

from marshmallow import Schema, fields


class GroupRegisterResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class GroupPostRecruitResponseSchema(Schema):
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


class GroupNoticeCommentResponseSchema(Schema):
    author: str = fields.String(required=True)
    text: str = fields.String(required=True)


class GroupNoticeDetailResponseSchema(Schema):
    id: int = fields.Integer(required=True)
    title: str = fields.String(required=True)
    description: str = fields.String(required=True)
    comments: List[GroupNoticeCommentResponseSchema] = fields.Nested(
        GroupNoticeCommentResponseSchema, many=True, required=True
    )
