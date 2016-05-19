import six
from datetime import datetime

import pytz

import config

__all__ = [
    'get_config',
    'utc_now',
    'MultiDict',
    'force_str',
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


class MultiDict(dict):
    def getlist(self, key):
        return self[key] if type(self[key]) == list else [self[key]]

    def __repr__(self):
        return type(self).__name__ + '(' + dict.__repr__(self) + ')'


def force_str(value, encoding='utf-8'):
    """
    Forces the value to a str instance, decoding if necessary.
    """
    if six.PY3 and isinstance(value, bytes):
        return str(value, encoding)
    else:
        return value
