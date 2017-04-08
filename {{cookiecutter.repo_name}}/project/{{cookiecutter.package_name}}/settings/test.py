from __future__ import absolute_import

from .base import *

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": env.db(default='sqlite://:memory:'),
}


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     'default': env.cache_url_config('locmem://'),
# }
########## END CACHE CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING['handlers']['console'] = {
    'level': 'DEBUG',
    'class': 'logging.StreamHandler',
    'formatter': 'verbose',
}
LOGGING['loggers'] = {
    '': {
        'handlers': ['console'],
        'level': 'DEBUG'
    }
}
########## END LOGGING CONFIGURATION
