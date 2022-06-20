"""API endpoints for managing submission resource."""

from http import HTTPStatus
import json
from flask import current_app, g, request
from flask_restx import Namespace, Resource

from formsflow_api.exceptions import BusinessException
from formsflow_api.schemas import (
    SubmissionSchema
)
from formsflow_api.services import SubmissionService
from formsflow_api.utils import (
    REVIEWER_GROUP,
    auth,
    cors_preflight,
    profiletime,
)

API = Namespace("Submission", description="Submission")

@cors_preflight("POST, GET, OPTIONS")
@API.route("", methods=["POST", "GET", "OPTIONS"])
class SubmissionResource(Resource):
    """Resource for getting all submissions."""

    @staticmethod
    @auth.require
    @profiletime
    def get():
        try:
            submission = SubmissionService.get_all_submission()
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
    def post():
        submission_json = request.get_json()
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

@cors_preflight("GET,PUT,OPTIONS")
@API.route("/<int:id>", methods=["GET", "PUT", "OPTIONS"])
class SubmissionResourceById(Resource):
    """Resource for managing submission by id."""

    @staticmethod
    @auth.require
    @profiletime
    def get(id: int):
        """Get submission by id."""
        try:
            return SubmissionService.get_submission(id), HTTPStatus.OK
        except BusinessException:
            response, status = (
                {
                    "type": "Invalid response data",
                    "message": f"Invalid id - {id}",
                },
                HTTPStatus.BAD_REQUEST,
            )

            current_app.logger.warning(response)
            return response, status


    @staticmethod
    @auth.require
    @profiletime
    def put(id:int):
        """Update submission details"""
        submission_json = request.get_json()
        try:
            submission_schema = SubmissionSchema()
            dict_data = submission_schema.load(submission_json)
            SubmissionService.update_submission(
                id=id, data=dict_data
            )
            return (
                f"Updated {id} successfully",
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
