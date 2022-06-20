"""This exposes submission service."""

from http import HTTPStatus
import json
from formsflow_api.exceptions import BusinessException
from formsflow_api.models import Submission
from formsflow_api.schemas import SubmissionSchema


class SubmissionService:
    """This class manages submission service."""
    @staticmethod
    def create_submission(data):
        """Create new mapper between form and process."""
        return Submission.create_from_dict(data)

    @staticmethod
    def update_submission(id: int, data):
        """Update submission."""
        submission = Submission.find_by_id(id=id)
        if submission:
            submission.update(data)
        else:
            raise BusinessException("Invalid submission", HTTPStatus.BAD_REQUEST)

    @staticmethod
    def get_submission(id: int):
        """Get submission."""
        submission = Submission.find_by_id(id=id)
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
