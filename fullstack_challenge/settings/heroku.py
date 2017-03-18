import os
from urllib import parse
from fullstack_challenge.settings.base import *


INSTALLED_APPS += (
    'gunicorn',
)

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Enable Persistent Connections
#DATABASES['default']['CONN_MAX_AGE'] = 500

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Force https? https://docs.djangoproject.com/en/1.10/topics/security/#ssl-https
SECURE_SSL_REDIRECT = os.environ.get('DJANGO_SECURE_SSL_REDIRECT', 'False') == 'True'
SESSION_COOKIE_SECURE = SECURE_SSL_REDIRECT
CSRF_COOKIE_SECURE = SECURE_SSL_REDIRECT

# Cache configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
redis_url = parse.urlparse(os.environ.get('REDISCLOUD_URL'))
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
        'TIMEOUT': 600, # 10 minutes
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': redis_url.password,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    },
    # 'api': {
    #     'BACKEND': 'redis_cache.RedisCache',
    #     'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
    #     'TIMEOUT': 60 * API_CACHE_RESPONSE_TIMEOUT,
    #     'OPTIONS': {
    #         'DB': 0,
    #         'PASSWORD': redis_url.password,
    #         'PARSER_CLASS': 'redis.connection.HiredisParser'
    #     }
    # },
    # 'staticfiles': {
    #     'BACKEND': 'redis_cache.RedisCache',
    #     'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
    #     'TIMEOUT': 2592000, # 30 days
    #     'OPTIONS': {
    #         'DB': 0,
    #         'PASSWORD': redis_url.password,
    #         'PARSER_CLASS': 'redis.connection.HiredisParser'
    #     }
    # }
}

# See: https://docs.djangoproject.com/en/dev/topics/http/sessions/#using-cached-sessions
#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-DEFAULT_FROM_EMAIL
DEFAULT_FROM_EMAIL = os.environ.get('DJANGO_DEFAULT_FROM_EMAIL', 'fullstack_challenge@sew.la')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'smtp.sendgrid.net')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = os.environ.get('DJANGO_EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[fullstack_challenge] '

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER


########## DJANGO-STORAGES CONFIGURATION
# See: http://django-storages.readthedocs.org/en/latest/
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# #AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
# AWS_S3_FILE_OVERWRITE = True
# AWS_PRELOAD_METADATA = True
# AWS_QUERYSTRING_AUTH = False
# AWS_IS_GZIPPED = True
# #AWS_S3_SECURE_URLS = False
# # from boto.s3.connection import VHostCallingFormat
# # AWS_S3_CALLING_FORMAT = VHostCallingFormat()
# # See: https://developers.google.com/speed/docs/best-practices/caching and http://developer.yahoo.com/performance/rules.html#expires
# from datetime import date, timedelta
# one_year = date.today() + timedelta(days=365)
# AWS_HEADERS = {
#     'Expires': one_year.strftime('%a, %d %b %Y 20:00:00 GMT'),
#     'Cache-Control': 'public, max-age=31536000', #max-age=31536000
# }
########## END DJANGO-STORAGES CONFIGURATION


########## STATIC AND MEDIA CONFIGURATION
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'fullstack_challenge.storage.StaticS3BotoStorage'
# # STATIC_URL = 'http://{0}/static/'.format(AWS_S3_CUSTOM_DOMAIN) #AWS_STORAGE_BUCKET_NAME
# # MEDIA_URL = 'http://{0}/'.format(AWS_S3_CUSTOM_DOMAIN) #AWS_STORAGE_BUCKET_NAME
# STATIC_URL = 'http://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
# MEDIA_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
########## END STATIC AND MEDIA CONFIGURATION