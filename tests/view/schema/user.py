from marshmallow import Schema, fields


class UserRegisterResponseSchema(Schema):
    id: str = fields.String(required=True)


class UserLoginResponseSchema(Schema):
    id: str = fields.String(required=True)
    nickname: str = fields.String(required=True)
    region: str = fields.String(required=True)
