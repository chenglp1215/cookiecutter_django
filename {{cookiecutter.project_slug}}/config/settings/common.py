# -*- coding: utf-8 -*-
"""
Django settings for {{cookiecutter.project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from __future__ import absolute_import, unicode_literals

import environ

ROOT_DIR = environ.Path(__file__) - 3  # ({{ cookiecutter.project_slug }}/config/settings/common.py - 3 = {{ cookiecutter.project_slug }}/)
APPS_DIR = ROOT_DIR.path('{{ cookiecutter.project_slug }}')

env = environ.Env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin
    # 'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'crispy_forms',  # Form layouts
    'xadmin',
    'cacheops',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    # custom users app
    '{{ cookiecutter.project_slug }}.user',
    # Your stuff: custom apps go here
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    str(APPS_DIR.path('fixtures')),
)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ("""{{cookiecutter.author_name}}""", '{{cookiecutter.email}}'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {

    'default': env.db('MASTER_DATABASE_URL', default='{{ cookiecutter.project_slug }}'),
    'slave1': env.db('SLAVE1_DATABASE_URL', default='{{ cookiecutter.project_slug }}'),
    'slave2': env.db('SLAVE2_DATABASE_URL', default='{{ cookiecutter.project_slug }}'),

}
DATABASES['default']['ATOMIC_REQUESTS'] = True

DATABASE_ROUTERS = []

TIME_ZONE = '{{ cookiecutter.timezone }}'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'zh-Hans'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

DATE_FORMAT = 'Y-m-d'

DATETIME_FORMAT = 'Y-m-d H:i'

TIME_FORMAT = 'H:i'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = env('DJANGO_STATIC_ROOT', default=str(APPS_DIR.path('static')))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = env('DJANGO_STATIC_URL', default='/static/')

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    str(APPS_DIR.path('static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = env('DJANGO_MEDIA_ROOT', default=str(APPS_DIR.path('media')))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = env('DJANGO_MEDIA_URL', default='{{ cookiecutter.static_url }}/{{ cookiecutter.project_slug }}/')

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------
# AUTHENTICATION_BACKENDS = (
# )

# Select the correct user model
# AUTH_USER_MODEL = ''
# LOGIN_REDIRECT_URL = ''
# LOGIN_URL = 'login'

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify'
{% if cookiecutter.use_celery == 'y' %}
# CELERY
INSTALLED_APPS += ('{{ cookiecutter.project_slug }}.taskapp',)
BROKER_URL = env('CELERY_BROKER_URL', default='django://')
if BROKER_URL == 'django://':
    CELERY_RESULT_BACKEND = 'redis://'
else:
    CELERY_RESULT_BACKEND = BROKER_URL
# END CELERY
{% endif %}

# Location of root django.contrib.admin URL, use {% raw %}{% url 'admin:index' %}{% endraw %}
ADMIN_URL = r'^adminx/'

# Your common stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
OAUTH_DECODE_KEY = env('DJANGO_OAUTH_DECODE_KEY', default='')

# Cacheops settings
CACHEOPS_REDIS = {
    'host': env('DJANGO_REDIS_HOST', default='127.0.0.1'),
    'port': 6379,
    'db': 2,
    'socket_timeout': 2,
}

CACHEOPS = {
    # Automatically cache any User.objects.get() calls for 15 minutes
    # This includes request.user or post.author access,
    # where Post.author is a foreign key to auth.User
    # 'users.user': {'ops': 'get', 'timeout': 60*10},
    # 'users.zone': {'ops': 'get', 'timeout': 60*60*12},
    # 'users.subsite': {'ops': 'get', 'timeout': 60*60*12},

    # Enable manual caching on all other models with default timeout of an hour
    # Use Post.objects.cache().get(...)
    #  or Tags.objects.filter(...).order_by(...).cache()
    # to cache particular ORM request.
    # Invalidation is still automatic
    '*.*': {'ops': (), 'timeout': 60*15},
}

CACHEOPS_DEGRADE_ON_FAILURE = True

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_IMAGE_BACKEND = 'pillow'
