"""Production settings and globals."""

from __future__ import absolute_import

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = False
########## END DEBUG CONFIGURATION


########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])
########## END HOST CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': env.db(),
}
########## END DATABASE CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# See base.LOGGING
LOGGING['loggers'] = {
    '': {
        'handlers': ['file', ],
        'level': 'DEBUG' if DEBUG else 'INFO'
    }
}
########## END LOGGING CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env('SECRET_KEY')
########## END SECRET CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
# EMAIL_HOST = env.str('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
# EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
# EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', ADMIN_EMAIL)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
# EMAIL_PORT = env.int('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
# EMAIL_SUBJECT_PREFIX = env.str('EMAIL_SUBJECT_PREFIX', '[%s] ' % PROJECT_NAME)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
# EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', True)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
# SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {
#     'default': env.cache(),
# }
########## END CACHE CONFIGURATION