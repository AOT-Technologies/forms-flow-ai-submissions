from marshmallow import EXCLUDE, Schema, fields


class SubmissionSchema(Schema):
    """This class manages submission request and response schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    _id = fields.Str(data_key="_id")
    data = fields.Dict(data_key="data", required=True)
    form_id = fields.Str(data_key="form")
    created = fields.Str()
    modified = fields.Str()
