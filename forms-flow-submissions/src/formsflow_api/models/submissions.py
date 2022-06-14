"""This manages Submission Database Models."""


from __future__ import annotations
from email.policy import default
import json
from .audit_mixin import AuditDateTimeMixin, AuditUserMixin
from .base_model import BaseModel
from .db import db
from sqlalchemy.dialects.postgresql import JSON

class Submission(BaseModel, db.Model):
    """This class manages submission information."""

    __tablename__ = "submission"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSON, nullable=False)

    @classmethod
    def create_from_dict(cls, submission_info: dict) -> Submission:
        """Create new application."""
        if submission_info:
            submission = Submission()
            submission.data = json.dumps(submission_info["data"])
            submission.save()
            return submission
        return None
    

    def update(self, submission_info: dict):
        """Update submission."""
        self.update_from_dict(
            [
                "data",
            ],
            submission_info,
        )
        self.commit()

