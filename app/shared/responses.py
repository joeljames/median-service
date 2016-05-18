from flask import jsonify, make_response

from app.shared import status


__all__ = [
    'ErrorResponse',
    'BadJsonResponse',
]


class StatusResponse:

    def __new__(cls,
                status=None,
                message=None,
                headers=None):
        response = {
            'status': status,
            'message': message
        }
        response_headers = {
            'Content-Type': 'application/json'
        }
        if headers:
            response_headers.update(headers)
        return make_response(
            jsonify(response),
            status,
            response_headers
        )


class ErrorResponse:

    def __new__(cls,
                status=None,
                message=None,
                description=None,
                errors=None,
                headers=None):
        response = {
            'status': status,
            'message': message,
            'description': description,
            'errors': errors or []
        }
        response_headers = {
            'Content-Type': 'application/json'
        }
        if headers:
            response_headers.update(headers)
        return make_response(
            jsonify(response),
            status,
            response_headers
        )


class BadJsonResponse:
    def __new__(cls, errors=None):
        return ErrorResponse(
            status=status.HTTP_400_BAD_REQUEST,
            message='Invalid Request',
            description='Request must be valid json.',
            errors=errors
        )
