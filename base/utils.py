"""
Base App Utilities.
"""

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Custom API exception handler.
    https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling
    """
    # Get response from request.
    response = exception_handler(exc, context)
    # Set error codes to catch.
    error_codes = [
        400,
        405,
        500
    ]

    # Check if status code in response matches codes in error_codes array.
    if response is not None and response.status_code in error_codes:
        # Add custom data to response.
        if response.status_code == 405:
            # Change any 405 status code to 500 status.
            response.status_code = 500
        response.data = {
            "msg": "Data is incomplete, missing, incorrect, \
            incorrect method or a server error has ocurred.",
        }

    return response
