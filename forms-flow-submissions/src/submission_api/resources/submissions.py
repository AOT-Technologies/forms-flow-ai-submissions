"""API endpoints for managing submission resource."""

import json
import string
from http import HTTPStatus

from flask import current_app, g, request
from flask_restx import Namespace, Resource

from submission_api.exceptions import BusinessException
from submission_api.schemas import SubmissionSchema
from submission_api.services import SubmissionService
from submission_api.utils import (
    REVIEWER_GROUP,
    auth,
    cors_preflight,
    profiletime,
)

API = Namespace("Submission", description="Submission")

submission_schema = SubmissionSchema()
@cors_preflight("POST, GET, OPTIONS")
@API.route("form/<string:formId>/submission", methods=["POST", "GET", "OPTIONS"])
class SubmissionResource(Resource):
    """Resource for getting all submissions."""

    @staticmethod
    @auth.require
    @profiletime
    def get(formId: string):
        try:
            response = SubmissionService.get_all_submission(form_id=formId)
            return (
                response,HTTPStatus.OK
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
            response = SubmissionService.get_submission(form_id=formId, _id=_id)
            response = submission_schema.dump(response)
            return response, HTTPStatus.OK
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
            dict_data = submission_schema.load(submission_json)
            submission = SubmissionService.update_submission(
                form_id=formId, _id=_id, data=dict_data
            )
            response = submission_schema.dump(submission)
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
            dict_data = submission_schema.load(submission_json)
            submission = SubmissionService.patch_submission(
                form_id=formId, _id=_id, data=dict_data
            )
            response = submission_schema.dump(submission)
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