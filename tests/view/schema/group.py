from marshmallow import Schema, fields


class GroupRegisterResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class GroupPostRecruitResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class GroupParticipateResponseSchema(Schema):
    id: int = fields.Integer(required=True)


class GroupPostTaskResponseSchema(Schema):
    id: int = fields.Integer(required=True)
