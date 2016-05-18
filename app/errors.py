from functools import partial

from flask import render_template


__all__ = [
    'add_error_handlers'
]


def not_found(error):
    """
    Renders the `404.html` template if the user navigates to
    a non defined route. The 404 template will provide a link
    which the user can hit and route back to the main page.
    """
    return render_template('404.html'), 404


def server_error(error, app=None):
    """
    Renders the `500.html` template if a internal server
    error happens.
    """
    app.logger.exception(error)
    return render_template('500.html'), 500


def add_error_handlers(app):
    app.error_handler_spec[None][404] = not_found
    app.error_handler_spec[None][500] = partial(server_error, app=app)
