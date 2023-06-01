"""Provides the WSGI entry point for running the application."""

import logging

from submission_api import create_app

application = create_app()  # pylint: disable=invalid-name
logging.warn("Application created trying to run ???")
if __name__ == "__main__":
    logging.warn('Running the Application')
    application.run()
