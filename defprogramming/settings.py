# Django settings for defprogramming project.
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ADMINS = ()
MANAGERS = ADMINS

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

USE_I18N = True
USE_L10N = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'defprogramming',
        'USER': 'defprogramming',
        'PASSWORD': 'defprogramming',
        'HOST': 'localhost',
        'PORT': '',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

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

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ROOT_URLCONF = 'defprogramming.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
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
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'south',
    'quotes',
    'sorl.thumbnail',
    'django_medusa',
    'rest_framework',
)

MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_MULTITHREAD = False
MEDUSA_DEPLOY_DIR = os.path.join(BASE_DIR, 'cache', 'html')

DEFAULT_CACHE_TIME = 60 * 15

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/day',
        'user': '10000/day'
    }
}

try:
    from settings_local import *  # NOQA
except ImportError:
    from warnings import warn
    msg = "You don't have settings_local.py file, using defaults settings."
    try:
        # don't work in Python 2.4 or before
        warn(msg, category=ImportWarning)
    except NameError:
        warn(msg)
