"""
Django settings for fullstack_challenge project.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'bhukpr5)sscgy4=4^rt*gv$q=gu*0@_m@k$evab1^l1qe&nkd7')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',

    'fullstack_challenge',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'debreach.middleware.RandomCommentMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'fullstack_challenge.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'build/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fullstack_challenge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', '')
STATIC_URL = STATIC_HOST + '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'build'),
)

# Simplified static file serving.
# http://whitenoise.readthedocs.org/en/latest/django.html

STATICFILES_STORAGE = 'fullstack_challenge.storage.CustomCompressedManifestStaticFilesStorage'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Michael Godshall', 'michaelgodshall@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# debug-toolbar settings
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ['127.0.0.1']

# RQ settings
REDIS_URL = os.getenv('REDISCLOUD_URL', 'redis://localhost:6379')
# RQ_QUEUES = {
#     'default': {
#         'URL': REDIS_URL,
#         'DB': 0,
#     },
#     'high': {
#         'URL': REDIS_URL,
#         'DB': 0,
#     },
#     'low': {
#         'URL': REDIS_URL,
#         'DB': 0,
#     }
# }

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': REDIS_URL,
    },
    # 'api': {
    #     'BACKEND': 'redis_cache.RedisCache',
    #     'LOCATION': REDIS_URL,
    # }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/sites/
#SITE_ID = 1

# Django Rest Framework
# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS': (
#         'rest_framework.filters.DjangoFilterBackend',
#         'rest_framework.filters.SearchFilter'
#     ),
#     #'PAGINATE_BY_PARAM': 'limit',
#     #'PAGINATE_BY': 100, # Default limit of results to return
#     #'MAX_PAGINATE_BY': 1000 # Max limit allowed by using `?limit=xxx`
#
# }
#
# REST_FRAMEWORK_EXTENSIONS = {
#     'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 1, # In seconds
#     #'DEFAULT_USE_CACHE': 'api'
# }
#
# AUTHENTICATION_BACKENDS = (
#     'social.backends.instagram.InstagramOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )
#
# SOCIAL_AUTH_INSTAGRAM_KEY = os.environ.get('SOCIAL_AUTH_INSTAGRAM_KEY', 'fd4f116989ef4010bfc4d3e900fbdbc8')
# SOCIAL_AUTH_INSTAGRAM_SECRET = os.environ.get('SOCIAL_AUTH_INSTAGRAM_KEY', '07af9738775f4e07ae6f1e60acbb82ae')
# SOCIAL_AUTH_INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {'scope': 'likes'}
# SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = ['username'] # Adds the 'username' to the social profile 'extra_data' field
# SOCIAL_AUTH_RAISE_EXCEPTIONS = False
#
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/' # Used to redirect the user once the auth process ended successfully. The value of ?next=/foo is used if it was present
# SOCIAL_AUTH_LOGIN_ERROR_URL = '/' # URL where the user will be redirected in case of an error

try:
    from fullstack_challenge.settings.local import *
except ImportError:
    pass