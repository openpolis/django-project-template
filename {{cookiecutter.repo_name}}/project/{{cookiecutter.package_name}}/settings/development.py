"""Development settings and globals."""

from __future__ import absolute_import

from os.path import join, normpath

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DEBUG', True)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': env.db(default='sqlite:///{0}'.format(normpath(join(RESOURCES_PATH, 'db', 'default.db'))))
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#      'default': env.cache(default='locmem://'),
# }
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
########## END TOOLBAR CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING['loggers'] = {
    '': {
        'handlers': ['console', 'file'],
        'level': 'WARNING',
    },
    'django': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
        'propagate': True,
    },
}
########## END LOGGING CONFIGURATION