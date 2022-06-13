from marshmallow import EXCLUDE, Schema, fields


class SubmissionSchema(Schema):
    """This class manages submission request and response schema."""

    class Meta:  # pylint: disable=too-few-public-methods
        """Exclude unknown fields in the deserialized output."""

        unknown = EXCLUDE

    id = fields.Str(data_key="id")
    data = fields.Dict(data_key="data", required=True)
