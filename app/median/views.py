from __future__ import absolute_import

from flask.views import MethodView
from flask import jsonify

from app.shared.services import get_logger


__all__ = [
    'MedianView',
]


class MedianView(MethodView):
    """
    The URL parsing view.
    The routing for this view is defined in `url.py`.
    """

    def __init__(self,
                 logger=None):
        super().__init__()
        self.logger = logger or get_logger('views')

    def get(self):
        """
        Handles the GET request.
        """
        return jsonify(
            dict(message='Hi')
        ), 200
