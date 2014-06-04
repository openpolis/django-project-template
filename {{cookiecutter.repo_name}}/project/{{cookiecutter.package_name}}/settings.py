# -*- coding: utf-8 -*-
"""
Django settings for {{cookiecutter.project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from sys import path
from os.path import join, dirname, abspath, basename
from configurations import Configuration, values


class Project(object):
    """
    {{cookiecutter.project_name}} specific settings.
    """
    ########## PATH CONFIGURATION
    PACKAGE_PATH = dirname(abspath(__file__))
    PACKAGE_NAME = basename(PACKAGE_PATH)

    PROJECT_PATH = dirname(PACKAGE_PATH)
    PROJECT_NAME = "{{cookiecutter.project_name}}" or PACKAGE_NAME
    PROJECT_PACKAGE = "{{cookiecutter.package_name}}" or PACKAGE_NAME

    REPO_PATH = dirname(PROJECT_PATH)
    REPO_NAME = "{{cookiecutter.repo_name}}" or basename(REPO_PATH)

    CONFIG_DIR = 'config'
    CONFIG_PATH = join(REPO_PATH, CONFIG_DIR)
    DOTENV_FILE = '.env'
    DOTENV_PATH = join(REPO_PATH, CONFIG_DIR, DOTENV_FILE)

    RESOURCE_DIR = 'resources'
    RESOURCES_PATH = join(REPO_PATH, RESOURCE_DIR)

    ########## END PATH CONFIGURATION


# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(Project.PROJECT_PATH)


class Common(Configuration, Project):

    ########## APP CONFIGURATION
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
    )
    THIRD_PARTY_APPS = (
        'south',  # Database migration helper
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        # Your stuff: custom apps go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
    ########## END APP CONFIGURATION

    ########## MIDDLEWARE CONFIGURATION
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    ########## END MIDDLEWARE CONFIGURATION

    ########## DEBUG
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(False)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG
    ########## END DEBUG

    ########## SECRET CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    # Note: This key only used for development and testing.
    #       In production, this is changed to a values.SecretValue() setting
    SECRET_KEY = "CHANGE ME"
    ########## END SECRET CONFIGURATION

    ########## FIXTURE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
    FIXTURE_DIRS = (
        join(Project.RESOURCES_PATH, 'fixtures'),
    )
    ########## END FIXTURE CONFIGURATION

    ########## EMAIL CONFIGURATION
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    ########## END EMAIL CONFIGURATION

    ########## MANAGER CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
    ADMINS = (
        ('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
    MANAGERS = ADMINS
    ########## END MANAGER CONFIGURATION

    ########## DATABASE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    DATABASES = values.DatabaseURLValue('sqlite:///{0}'.format(join(Project.RESOURCES_PATH, 'db', 'sqlite.db')))
    ########## END DATABASE CONFIGURATION

    ########## CACHING
    # Do this here because thanks to django-pylibmc-sasl and pylibmc memcacheify is painful to install on windows.
    # memcacheify is what's used in Production
    CACHES = values.CacheURLValue('locmem://')
    ########## END CACHING

    ########## GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'Europe/Rome'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'it-IT'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    ########## END GENERAL CONFIGURATION

    ########## TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        # Your stuff: custom template context processers go here
        '{{cookiecutter.package_name}}.contexts.project_context'
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(Project.PACKAGE_PATH, 'templates'),
    )

    TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )
    ########## END TEMPLATE CONFIGURATION

    ########## STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(Project.RESOURCES_PATH, 'static')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(Project.PACKAGE_PATH, 'static'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    ########## END STATIC FILE CONFIGURATION

    ########## MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(Project.RESOURCES_PATH, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    ########## END MEDIA CONFIGURATION

    ########## URL Configuration
    ROOT_URLCONF = '{{ cookiecutter.package_name}}.urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = '{{ cookiecutter.package_name}}.wsgi.application'
    ########## End URL Configuration

    ########## AUTHENTICATION CONFIGURATION
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
    )
    ########## END AUTHENTICATION CONFIGURATION

    ########## LOGGING CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    # A sample logging configuration. The only tangible logging
    # performed by this configuration is to send an email to
    # the site admins on every HTTP 500 error when DEBUG=False.
    # See http://docs.djangoproject.com/en/dev/topics/logging for
    # more details on how to customize your logging configuration.
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt' : "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            # add a file log
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': join(Project.RESOURCES_PATH, 'logs', '{{cookiecutter.package_name}}.log'),
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
    ########## END LOGGING CONFIGURATION


    ########## Your common stuff: Below this line define 3rd party libary settings


class Development(Common):

    ########## DEBUG
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG
    ########## END DEBUG

    ########## INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    ########## END INSTALLED_APPS

    ########## Mail settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    ########## End mail settings

    ########## Debug logging on file
    LOGGING = Common.LOGGING
    LOGGING['loggers']['django.request']['handlers'] = ['file']
    LOGGING['loggers']['django'] = {
        'handlers':['file'],
        'propagate': True,
        'level':'DEBUG',
    }
    LOGGING['loggers']['{{cookiecutter.package_name}}'] = {
        'handlers':['file'],
        'level':'DEBUG',
    }
    ########## end Debug logging

    ########## django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    ########## end django-debug-toolbar

    ########## Your local stuff: Below this line define 3rd party libary settings


class Production(Common):

    ########## INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    ########## END INSTALLED_APPS

    ########## SECRET KEY
    SECRET_KEY = values.SecretValue()
    ########## END SECRET KEY

    ########## SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    ########## END SITE CONFIGURATION

    ########## EMAIL
    # DEFAULT_FROM_EMAIL = values.Value(
    #         '{{cookiecutter.project_name}} <noreply@{{cookiecutter.domain_name}}>')
    # EMAIL_HOST = values.Value('smtp.sendgrid.com')
    # EMAIL_HOST_PASSWORD = values.SecretValue(environ_prefix="", environ_name="SENDGRID_PASSWORD")
    # EMAIL_HOST_USER = values.SecretValue(environ_prefix="", environ_name="SENDGRID_USERNAME")
    # EMAIL_PORT = values.IntegerValue(587, environ_prefix="", environ_name="EMAIL_PORT")
    # EMAIL_SUBJECT_PREFIX = values.Value('[{{cookiecutter.project_name}}] ', environ_name="EMAIL_SUBJECT_PREFIX")
    # EMAIL_USE_TLS = True
    # SERVER_EMAIL = EMAIL_HOST_USER
    ########## END EMAIL

    ########## TEMPLATE CONFIGURATION

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )
    ########## END TEMPLATE CONFIGURATION

    ########## Your production stuff: Below this line define 3rd party libary settings

