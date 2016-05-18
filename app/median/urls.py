"""
This module handles the routing to the server.
Based on the URL requested, the router will call out to the
respective view.
"""

from __future__ import absolute_import
from flask import Blueprint

from app.median.views import (
    ValueView,
    MedianView,
)


__all__ = [
    'mod_median',
]


# Instantiates the BluePrint
mod_median = Blueprint(
    'median',
    __name__,
    url_prefix='/'
)


# Adds the routing. Calls the `ValueView` when the user access the root
mod_median.add_url_rule(
    '/',
    view_func=ValueView.as_view('value_update')
)

# Adds the routing. Calls the `MedianView` when the user access the `/median`
mod_median.add_url_rule(
    'median',
    view_func=MedianView.as_view('median_detail')
)
