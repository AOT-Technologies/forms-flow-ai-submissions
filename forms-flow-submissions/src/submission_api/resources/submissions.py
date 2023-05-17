"""API endpoints for managing submission resource."""

from http import HTTPStatus
import json
import string
from flask import current_app, g, request
from flask_restx import Namespace, Resource

from submission_api.exceptions import BusinessException
from submission_api.schemas import (
    SubmissionSchema
)
from submission_api.services import SubmissionService
from submission_api.utils import (
    REVIEWER_GROUP,
    auth,
    cors_preflight,
    profiletime,
)

API = Namespace("Submission", description="Submission")

@cors_preflight("POST, GET, OPTIONS")
@API.route("form/<string:formId>/submission", methods=["POST", "GET", "OPTIONS"])
class SubmissionResource(Resource):
    """Resource for getting all submissions."""

    @staticmethod
    @auth.require
    @profiletime
    def get(formId: string):
        try:
            submission = SubmissionService.get_all_submission(form_id=formId)
            return (
                submission,HTTPStatus.OK
            )

        except BaseException as submission_err:  # pylint: disable=broad-except
            response, status = {
                "type": "Bad request error",
                "message": "Invalid submission request passed",
            }, HTTPStatus.BAD_REQUEST
            current_app.logger.warning(response)
            current_app.logger.warning(submission_err)
            return response, status



    @staticmethod
    @auth.require
    @profiletime
    def post(formId: string):
        submission_json = request.get_json()
        submission_json['form'] = formId
        try:
            submission_schema = SubmissionSchema()
            dict_data = submission_schema.load(submission_json)
            submission = SubmissionService.create_submission(
                data=dict_data
            )
            response = submission_schema.dump(submission)
            return (
                response,HTTPStatus.CREATED
            )
            
        except BaseException as submission_err:  # pylint: disable=broad-except
            response, status = {
                "type": "Bad request error",
                "message": "Invalid submission request passed",
            }, HTTPStatus.BAD_REQUEST
            current_app.logger.warning(response)
            current_app.logger.warning(submission_err)
            return response, status

@cors_preflight("GET,PUT,PATCH,OPTIONS")
@API.route("form/<string:formId>/submission/<string:_id>", methods=["GET", "PUT", "PATCH","OPTIONS"])
class SubmissionResourceById(Resource):
    """Resource for managing submission by id."""

    @staticmethod
    @auth.require
    @profiletime
    def get(formId: string, _id: str):
        """Get submission by id."""
        try:
            return SubmissionService.get_submission(form_id=formId, _id=_id), HTTPStatus.OK
        except BusinessException:
            response, status = (
                {
                    "type": "Invalid response data",
                    "message": f"Invalid id - {_id}",
                },
                HTTPStatus.BAD_REQUEST,
            )

            current_app.logger.warning(response)
            return response, status


    @staticmethod
    @auth.require
    @profiletime
    def put(formId: string, _id:str):
        """Update submission details"""
        submission_json = request.get_json()
        try:
            submission_schema = SubmissionSchema()
            dict_data = submission_schema.load(submission_json)
            response = SubmissionService.update_submission(
                form_id=formId, _id=_id, data=dict_data
            )
            return (
                response,
                HTTPStatus.OK,
            )
        except BaseException as submission_err:  # pylint: disable=broad-except
            response, status = {
                "type": "Bad request error",
                "message": "Invalid request data",
            }, HTTPStatus.BAD_REQUEST

            current_app.logger.warning(response)
            current_app.logger.warning(submission_err)

            return response, status

    @staticmethod
    @auth.require
    @profiletime
    def patch(formId: string, _id:str):
        """Patch submission details"""
        submission_json = request.get_json()
        try:
            submission_schema = SubmissionSchema()
            dict_data = submission_schema.load(submission_json)
            SubmissionService.patch_submission(
                form_id=formId, _id=_id, data=dict_data
            )
            return (
                f"Updated {_id} successfully",
                HTTPStatus.OK,
            )
        except BaseException as submission_err:  # pylint: disable=broad-except
            response, status = {
                "type": "Bad request error",
                "message": "Invalid request data",
            }, HTTPStatus.BAD_REQUEST

            current_app.logger.warning(response)
            current_app.logger.warning(submission_err)

            return response, status