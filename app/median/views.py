from __future__ import absolute_import

from flask.views import MethodView
from flask import jsonify, request


from app.median.forms import ValuePostForm
from app.shared.services import get_logger
from app.shared import status
from app.shared.utils import MultiDict
from app.shared.mixins import RepositoryMixin
from app.median.repositories import ValueRepository
from app.shared.responses import (
    BadJsonResponse,
    ErrorResponse,
    StatusResponse
)


__all__ = [
    'ValueView',
    'MedianView',
]


class ValueView(MethodView,
                RepositoryMixin):

    repository_class = ValueRepository

    def __init__(self,
                 logger=None):
        super().__init__()
        self.logger = logger or get_logger('views')

    def put(self):
        """
        Handles the PUT request for creating a value.
        Creates the value if the request body is valid
        else logs the errors and returns a error object
        """
        req_json = request.get_json(force=True, silent=True)
        if not req_json:
            return BadJsonResponse()

        form = ValuePostForm(
            MultiDict(req_json),
            csrf_enabled=False
        )
        if form.validate_on_submit():
            form.save(self.repository)
            return StatusResponse(
                status=status.HTTP_201_CREATED,
                message='Value successfully created.',
            )
        else:
            self.logger.error(form.errors)
            return ErrorResponse(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                message='Error creating the value.',
                description='The input field contained invalid data',
                errors=form.errors
            )


class MedianView(MethodView,
                 RepositoryMixin):

    repository_class = ValueRepository

    def __init__(self,
                 logger=None):
        super().__init__()
        self.logger = logger or get_logger('views')

    def get(self):
        """
        Handles the GET request.
        Returns the median value for all the objects created in
        past 1 minute.
        """
        median = self.repository.calculate_median()
        return jsonify(
            dict(median=median)
        ), status.HTTP_200_OK
