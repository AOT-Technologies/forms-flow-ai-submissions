"""This exposes submission service."""

from http import HTTPStatus
import json
from submission_api.exceptions import BusinessException
from submission_api.models import Submission
from submission_api.schemas import SubmissionSchema


def update(dict1, dict2):
    """This function update dictionary of dictionaries"""
    for key, val in dict2.items():
        if isinstance(val, dict):
            dict1[key] = update(dict1.get(key, {}), val)
        else:
            dict1[key] = val
    return dict1


class SubmissionService:
    """This class manages submission service."""
    @staticmethod
    def create_submission(data):
        """Create new mapper between form and process."""
        return Submission.create_from_dict(data)

    @staticmethod
    def update_submission(form_id: str, _id: str, data):
        """Update submission."""
        submission = Submission.find_by_id(form_id=form_id, _id=_id)
        if submission:
            submission.update(data)
        else:
            raise BusinessException("Invalid submission", HTTPStatus.BAD_REQUEST)

    
    @staticmethod
    def patch_submission(form_id:str, _id: str, data):
        """Update submission."""
        submission = Submission.find_by_id(form_id=form_id, _id=_id)
        result = update(submission.data, data["data"])
        
        if submission:
            submission = submission.patch(data=result)
        else:
            raise BusinessException("Invalid submission", HTTPStatus.BAD_REQUEST)


    @staticmethod
    def get_submission(form_id:str, _id: str):
        """Get submission."""
        submission = Submission.find_by_id(form_id=form_id, _id=_id)
        if submission:
           submission_schema = SubmissionSchema()
           return submission_schema.dump(submission)

        raise BusinessException("Invalid submission", HTTPStatus.BAD_REQUEST)


    @staticmethod
    def get_all_submission(form_id:str):
        """Get all submissions."""
        submission = Submission.find_all(form_id=form_id)
        submission_schema = SubmissionSchema()
        return submission_schema.dump(submission, many=True)
