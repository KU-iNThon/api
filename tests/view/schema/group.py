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
