"""This exposes submission service."""

from http import HTTPStatus

from formsflow_api.exceptions import BusinessException
from formsflow_api.models import Submission
from formsflow_api.schemas import SubmissionSchema


class SubmissionService:
    """This class manages submission service."""
    @staticmethod
    def create_submission(data):
        """Create new mapper between form and process."""
        return Submission.create_from_dict(data)
