"""API endpoints for managing submission resource."""

import json
import string
from http import HTTPStatus

from flask import current_app, g, request
from flask_restx import Namespace, Resource

from submission_api.schemas import SubmissionSchema
from submission_api.services import SubmissionService
from submission_api.utils import cors_preflight, profiletime

API = Namespace("Public", description="Public api endpoints")


@cors_preflight("POST, OPTIONS")
@API.route("/form/<string:formId>/submission", methods=["POST", "OPTIONS"])
class AnonymoussSubmissionResource(Resource):
    """Resource for anonymous submission creation."""

    @staticmethod
    @profiletime
    def post(formId: string):
        """Post a new anonymous submission using request body.
        """
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
                response, HTTPStatus.CREATED
            )
            
        except BaseException as submission_err:  # pylint: disable=broad-except
            response, status = {
                "type": "Bad request error",
                "message": "Invalid submission request passed",
            }, HTTPStatus.BAD_REQUEST
            current_app.logger.warning(response)
            current_app.logger.warning(submission_err)
            return response, status
