"""This exposes submission service."""

from http import HTTPStatus
import json
from submission_api.exceptions import BusinessException
from submission_api.models import Submission
from submission_api.schemas import SubmissionSchema


class SubmissionService:
    """This class manages submission service."""
    @staticmethod
    def create_submission(data):
        """Create new mapper between form and process."""
        return Submission.create_from_dict(data)

    @staticmethod
    def update_submission(_id: str, data):
        """Update submission."""
        submission = Submission.find_by_id(_id=_id)
        if submission:
            submission.update(data)
        else:
            raise BusinessException("Invalid submission", HTTPStatus.BAD_REQUEST)

    @staticmethod
    def get_submission(_id: str):
        """Get submission."""
        submission = Submission.find_by_id(_id=_id)
        if submission:
           submission_schema = SubmissionSchema()
           return submission_schema.dump(submission)

        raise BusinessException("Invalid submission", HTTPStatus.BAD_REQUEST)


    @staticmethod
    def get_all_submission():
        """Get all submissions."""
        submission = Submission.find_all()
        submission_schema = SubmissionSchema()
        return submission_schema.dump(submission, many=True)
