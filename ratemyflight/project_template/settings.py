# Django settings for ratemyflight project.

import os
project_path = os.path.dirname(os.path.abspath(__file__))
project_dir = project_path.split(os.sep)[-1]

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("Stephen McDonald", "stephen.mc@gmail.com"),
    ("Andrew Fisher", "ajfisher.td@gmail.com"),
    ("Josh de Blank", "jdeblank@gmail.com"),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3' # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(project_path, "ratemyflight.db")                      # Or path to database file if using sqlite3.
DATABASE_USER = ''                     # Not used with sqlite3.
DATABASE_PASSWORD = ''                  # Not used with sqlite3.
DATABASE_HOST = ''                      # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''                     # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Australia/Melbourne"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(project_path, MEDIA_URL.strip("/"))

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#)a%&0%^@45nasdfasdf2c+yf*@=-4)z&lc=&o58du#9+hf-6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = "%s.urls" % project_dir

TEMPLATE_DIRS = (os.path.join(project_path, "templates"),)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    "ratemyflight",
)

# Optional apps.
OPTIONAL_APPS = (
    "debug_toolbar",
    "south",
    "django_extensions", 
)

import sys
sys.path.append(os.path.join(project_path, ".."))
if not (len(sys.argv) > 1 and sys.argv[1] == "test"):
    for app in OPTIONAL_APPS:
        try:
            __import__(app)
        except ImportError:
            pass
        else:
            INSTALLED_APPS += (app,)
INSTALLED_APPS = sorted(list(INSTALLED_APPS), reverse=True)

# Optional app settings.
if "debug_toolbar" in INSTALLED_APPS:
    DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}
    MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

# Local settings.
try:
    from local_settings import *
except ImportError:
    pass
