"""API endpoints for managing healthcheckpoint API resource."""

from http import HTTPStatus

from flask_restx import Namespace, Resource

from submission_api.utils import cors_preflight

API = Namespace("Checkpoint", description="Checkpoint")


@cors_preflight("GET")
@API.route("", methods=["GET"])
class HealthCheckpointResource(Resource):
    """Resource for managing healthcheckpoint."""

    @staticmethod
    def get():
        """Get the status of API."""
        return (
            ({"message": "Welcome to formsflow.ai Submissions API"}),
            HTTPStatus.OK,
        )
