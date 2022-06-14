"""Provides the WSGI entry point for running the application."""

from formsflow_api import create_app
import logging

application = create_app()  # pylint: disable=invalid-name
logging.warn("Application created trying to run ???")
if __name__ == "__main__":
    logging.warn('Running the Application')
    application.run()
