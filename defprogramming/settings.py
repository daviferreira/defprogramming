# Django settings for defprogramming project.
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__) + '/../')
ADMINS = () 
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASEDIR, 'db/development.sqlite3'),
    }
}

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'secret'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'defprogramming.urls'

TEMPLATE_DIRS = (
    os.path.join(BASEDIR, 'templates/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.syndication',
    'django.contrib.sitemaps',
    'quotes',
)


try:
    from settings_local import *
except ImportError:
    from warnings import warn
    msg = "You don't have settings_local.py file, using defaults settings."
    try:
        # don't work in Python 2.4 or before
        warn(msg, category=ImportWarning)
    except NameError:
        warn(msg)
