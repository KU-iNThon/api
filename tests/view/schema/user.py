from marshmallow import Schema, fields


class UserRegisterResponseSchema(Schema):
    id: str = fields.String(required=True)


class UserLoginResponseSchema(Schema):
    id: str = fields.String(required=True)
    nickname: str = fields.String(required=True)
    region: str = fields.String(required=True)


class UserProfileGroupResponseDto(Schema):
    id: int = fields.Int(required=True)
    name: str = fields.Str(required=True)
    total_task: int = fields.Int(required=True)
    completed_task: int = fields.Int(required=True)
    role: str = fields.Str(required=True, validate=lambda x: x in ["admin", "user"])
    closed: bool = fields.Bool(required=True)


class UserProfileSummaryResponseDto(Schema):
    completed_task: int = fields.Int(required=True)
    total_task: int = fields.Int(required=True)


class UserProfileResponseSchema(Schema):
    id: str = fields.Str(required=True)
    nickname: str = fields.Str(required=True)
    region: str = fields.Str(required=True)
    groups: list = fields.Nested(UserProfileGroupResponseDto, required=True, many=True)
    summary: dict = fields.Nested(UserProfileSummaryResponseDto, required=True)
