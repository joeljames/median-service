import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# ----------------------------------------------------------------------------
# Base Server Setup
# ----------------------------------------------------------------------------

# Turns on/off application debug mode.
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Turns on/off application local mode.
LOCAL = os.environ.get('LOCAL', 'True') == 'True'

# Port at which the app would be listening.
PORT = os.environ.get('PORT', 8000)

# Sets the default logging level for the application
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')

# Secret keys.
CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY', 'default_secret_csrf')
SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')


# Static files
STATIC_FOLDER = os.environ.get('STATIC_FOLDER', 'assets')
STATIC_URL_PATH = os.environ.get('STATIC_FOLDER', '')

# ----------------------------------------------------------------------------
# Database
# ----------------------------------------------------------------------------

DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'mongodb://db:27017/db'
)
