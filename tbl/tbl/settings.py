"""
Django settings for tbl project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from .config.apps import PRODUCTION_APPS, DEVELOPMENT_APPS
from .config.middleware import MIDDLEWARE
from .config.template import TEMPLATES
from .config.security import SECRET_KEY
from .config.database import DB_DEVELOPMENT, DB_PRODUCTION
from .config.password import AUTH_PASSWORD_VALIDATORS
from .config.files import STATIC_ROOT, MEDIA_ROOT, STATIC_URL, MEDIA_URL
from .config.rest import REST_FRAMEWORK, JWT_AUTH
from .config.internacionalization import (
    PORTUGUESE,
    TIME_ZONE,
    INTERNATIONALIZATION,
    FORMAT_DATES,
    TIMEZONE_DATETIMES
)

# development or production enviroment
MODE_ENVIROMENT = 'development'

# secret key
SECRET_KEY = SECRET_KEY

# middlewares
MIDDLEWARE = MIDDLEWARE

# Urls
ROOT_URLCONF = 'tbl.urls'

# Templates
TEMPLATES = TEMPLATES

# WSGI - Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tbl.wsgi.application'

# Custom user profile
# Tell Django to use our custom user model
# instead of its built in default user model.
AUTH_USER_MODEL = 'accounts.User'

# Password validation
AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
LANGUAGE_CODE = PORTUGUESE
TIME_ZONE = TIME_ZONE
USE_I18N = INTERNATIONALIZATION
USE_L10N = FORMAT_DATES
USE_TZ = TIMEZONE_DATETIMES


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = STATIC_ROOT
STATIC_URL = STATIC_URL
MEDIA_ROOT = MEDIA_ROOT
MEDIA_URL = MEDIA_URL

# Django Rest Framework
# http://www.django-rest-framework.org/
# http://getblimp.github.io/django-rest-framework-jwt/
REST_FRAMEWORK = REST_FRAMEWORK
JWT_AUTH = JWT_AUTH


# Enviroments mode (development or production)
if MODE_ENVIROMENT == 'development':
    DEBUG = True
    DATABASES = DB_DEVELOPMENT
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    INSTALLED_APPS = DEVELOPMENT_APPS
    # Allow all host/domain to access this aplication
    ALLOWED_HOSTS = []
elif MODE_ENVIROMENT == 'production':
    DEBUG = False
    DATABASES = DB_PRODUCTION
    INSTALLED_APPS = PRODUCTION_APPS
    # Allow all host/domain to access this aplication
    ALLOWED_HOSTS = ['*']
