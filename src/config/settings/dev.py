import os

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '../../.env'))

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']

# False if not in os.environ because of casting above

DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': env('SQL_ENGINE'),
        'NAME': env('SQL_DATABASE', default='todolist_django'),
        'USER': env('SQL_USER', default='postgres'),
        'PASSWORD': env('SQL_PASSWORD', default='12345'),
        'HOST': env('SQL_HOST', default='127.0.0.1'),
        'PORT': env('SQL_PORT', default=5432),
    }
}

AUTH_USER_MODEL = 'core.User'
