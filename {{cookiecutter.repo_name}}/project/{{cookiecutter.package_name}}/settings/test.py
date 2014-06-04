from __future__ import absolute_import

from .base import *

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": env.db('sqlite://:memory:'),
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