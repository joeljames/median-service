from datetime import datetime

import pytz

import config

__all__ = [
    'get_config',
    'utc_now',
]


def get_config(key, default=None):
    """
    Get config from config module if exists,
    return default value otherwise
    """
    return getattr(config, key, default)


def utc_now():
    """
    Returns current UTC time and sets the time zone info to UTC
    """
    d = datetime.utcnow()
    return d.replace(tzinfo=pytz.UTC)
