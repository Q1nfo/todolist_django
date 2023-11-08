import os

from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": os.environ.get("SQL_DATABASE", "todolist_django"),
        "USER": os.environ.get("SQL_USER", "postgres"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "12345"),
        "HOST": os.environ.get("SQL_HOST", "127.0.0.1"),
        "PORT": os.environ.get("SQL_PORT", 5432),
    }
}

AUTH_USER_MODEL = 'core.User'
