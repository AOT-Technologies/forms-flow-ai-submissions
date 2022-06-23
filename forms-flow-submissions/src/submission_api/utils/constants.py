"""All constants for project."""
import os

from dotenv import find_dotenv, load_dotenv

# this will load all the envars from a .env file located in the project root (api)
load_dotenv(find_dotenv())

SUBMISSION_API_CORS_ORIGINS = os.getenv("SUBMISSION_API_CORS_ORIGINS", "*")
ALLOW_ALL_ORIGINS = "*"
CORS_ORIGINS = []
if SUBMISSION_API_CORS_ORIGINS != "*":
    CORS_ORIGINS = SUBMISSION_API_CORS_ORIGINS.split(",")
DESIGNER_GROUP = "formsflow-designer"
REVIEWER_GROUP = "formsflow-reviewer"
ALLOW_ALL_APPLICATIONS = "/formsflow/formsflow-reviewer/access-allow-applications"

NEW_APPLICATION_STATUS = "New"
KEYCLOAK_DASHBOARD_BASE_GROUP = "formsflow-analytics"
ANONYMOUS_USER = "Anonymous-user"

FILTER_MAPS = {
    "application_id": {"field": "id", "operator": "eq"},
    "application_name": {"field": "form_name", "operator": "ilike"},
    "application_status": {"field": "application_status", "operator": "eq"},
    "created_by": {"field": "created_by", "operator": "eq"},
    "modified_from": {"field": "modified", "operator": "ge"},
    "modified_to": {"field": "modified", "operator": "le"},
    "created_from": {"field": "created", "operator": "ge"},
    "created_to": {"field": "created", "operator": "le"},
    "form_name": {"field": "form_name", "operator": "ilike"},
}
