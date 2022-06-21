"""Exposes all of the resource endpoints mounted in Flask-Blueprint style.

Uses restx namespaces to mount individual api endpoints into the service.
"""

from flask_jwt_oidc import AuthError
from flask_restx import Api

from submission_api.exceptions import BusinessException

from submission_api.resources.checkpoint import API as CHECKPOINT_API
from submission_api.resources.submissions import API as SUBMISSION_API



# This will add the Authorize button to the swagger docs
# oauth2 & openid may not yet be supported by restplus
AUTHORIZATIONS = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}

API = Api(
    title="formsflow.ai API",
    version="1.0",
    description="The API for formsflow.ai. Checkout: formsflow.ai to know more",
    security=["apikey"],
    authorizations=AUTHORIZATIONS,
    doc="/",
)


@API.errorhandler(BusinessException)
def handle_business_exception(error: BusinessException):
    """Handle Business exception."""
    return (
        {"message": error.error},
        error.status_code,
        {"Access-Control-Allow-Origin": "*"},
    )


@API.errorhandler(AuthError)
def handle_auth_error(error: AuthError):
    """Handle Auth exception."""
    return (
        {
            "type": "Invalid Token Error",
            "message": "Access to formsflow.ai API Denied. Check if the "
            "bearer token is passed for Authorization or has expired.",
        },
        error.status_code,
        {"Access-Control-Allow-Origin": "*"},
    )

API.add_namespace(CHECKPOINT_API, path="/checkpoint")
API.add_namespace(SUBMISSION_API, path="/submission")

