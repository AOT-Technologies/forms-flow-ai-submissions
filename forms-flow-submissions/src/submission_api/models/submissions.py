"""This manages Submission Database Models."""


from __future__ import annotations

import json
import uuid
from email.policy import default

from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.orm.attributes import flag_modified

from .audit_mixin import AuditDateTimeMixin, AuditUserMixin
from .base_model import BaseModel
from .db import db


class Submission(BaseModel, db.Model, AuditDateTimeMixin):
    """This class manages submission information."""

    __tablename__ = "submission"
    id = db.Column(db.Integer, primary_key=True)
    _id =db.Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, nullable=False)
    data = db.Column(JSON, nullable=False)
    form_id = db.Column(db.String(100), nullable=False)

    @classmethod
    def create_from_dict(cls, submission_info: dict) -> Submission:
        """Create new application."""
        if submission_info:
            submission = Submission()
            submission.data = submission_info["data"]
            submission.form_id = submission_info["form_id"]
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

    @classmethod
    def find_by_id(cls, form_id:str, _id: str) -> Submission:
        """Find submission that matches the provided id."""
        result = (
            cls.query.filter(Submission.form_id ==form_id)
            .filter_by(_id=_id).first()
        )
        return result

    def patch(self, data: dict):
        """Patch submission."""
        self.data = data
        flag_modified(self, "data")
        self.commit()

    @classmethod
    def find_all(cls, form_id:str):
        """Fetch all submission."""
        result = (
            cls.query.filter(Submission.form_id == form_id)
            .order_by(Submission.id.desc())   
        )
        return result  
