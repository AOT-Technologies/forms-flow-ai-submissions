"""Manage the database and some other items required to run the API."""

import logging

from flask.cli import FlaskGroup
from flask_migrate import Migrate

# models included so that migrate can build the database migrations
from submission_api import models  # noqa: F401 # pylint: disable=unused-import
from submission_api import create_app
from submission_api.models import db

APP = create_app()
cli = FlaskGroup(APP)

MIGRATE = Migrate(APP, db)

if __name__ == '__main__':
    logging.log(logging.INFO, 'Running the Manager')
    cli()