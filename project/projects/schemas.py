from marshmallow import Schema, fields


class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    project_name = fields.Str(required=True)
    # tasks = fields.List(fields.Nested(TaskSchema))


project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

