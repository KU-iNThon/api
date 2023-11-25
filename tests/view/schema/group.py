from marshmallow import Schema, fields


class GroupRegisterResponseSchema(Schema):
    id: int = fields.Integer(required=True)
