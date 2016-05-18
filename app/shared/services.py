import logging
import sys

import mongoengine

from app.shared.utils import get_config
from app.shared.decorators import singleton


__all__ = [
    'get_logger',
    'get_mongo_connection',
]


def get_logger(name):
    """
    Configures the logger and set the logging level
    on the logger based on the config var `LOGGING_LEVEL`.
    You can change the logging level by updating the
    env variable `LOGGING_LEVEL`.
    """

    logger = logging.getLogger(name)
    if not logger.handlers:
        out = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s \
            - %(module)s - %(message)s'
        )
        out.setFormatter(formatter)
        logger.addHandler(out)
        logger.setLevel(get_config('LOGGING_LEVEL'))
        logger.propagate = False
    return logger


@singleton
def get_mongo_connection(url=None, collection=None):
    """
    Factory method for returning the mongoengine connection configured for
    the current environment.
    """
    db_url = url or get_config('DATABASE_URL')
    collection = collection or 'value'
    return mongoengine.connect('value', host=db_url)
