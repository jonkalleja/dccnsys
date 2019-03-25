"""
Django settings for wwwdccn project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.urls import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REMOTE_DEPLOY = os.environ.get('DJANGO_REMOTE', False)

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGOUT_REDIRECT_URL = reverse_lazy('home')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if REMOTE_DEPLOY:
    SECRET_KEY = os.environ['SECRET_KEY']
    ALLOWED_HOSTS = [os.environ['SITENAME']]
    DEBUG = False
else:
    # noinspection SpellCheckingInspection
    SECRET_KEY = '!unng-b4vbp6e=i^_gj!mrq56a88z4%6m2@_fhe8v!o*2k_%v*'
    ALLOWED_HOSTS = []
    DEBUG = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party applications:
    'bootstrap4',
    'anymail',
    'storages',

    # Application defined in this project:
    'users',
    'public_site',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wwwdccn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'wwwdccn', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wwwdccn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if os.environ.get('DATABASE_PROVIDER', '') == 'postgresql':
    DB_NAME = os.environ['DB_NAME']
    DB_USERNAME = os.environ['DB_USERNAME']
    DB_PASSWORD = os.environ['DB_PASSWORD']
    DB_HOST = os.environ['DB_HOST']
    DB_PORT = os.environ.get('DB_PORT', '')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        },
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

# Define custom user model:
AUTH_USER_MODEL = 'users.User'


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
#################################################################
# Static files settings
#
# -- Environment variables:
# * STATIC_PROVIDER (opt.), 'selcdn' or 'local'
#
# If MEDIA_PROVIDER == 'selcdn', then we need the following variables:
# * SELCDN_HTTP_HOST - e.g. 239120.selcdn.ru (without https:// or slashes)
# * SELCDN_USERNAME
# * SELCDN_PASSWORD
# * SELCDN_STATIC_BIN (!! without slashes)
#################################################################
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

if os.environ.get('STATIC_PROVIDER', '') == 'selcdn':
    SELCDN_HTTP_HOST = os.environ['SELCDN_HTTP_HOST']
    SELCDN_USERNAME = os.environ['SELCDN_USERNAME']
    SELCDN_PASSWORD = os.environ['SELCDN_PASSWORD']
    SELCDN_STATIC_BIN = os.environ['SELCDN_STATIC_BIN']

    STATICFILES_STORAGE = 'wwwdccn.storages.StaticSFTPStorage'
    STATIC_URL = f'https://{SELCDN_HTTP_HOST}/{SELCDN_STATIC_BIN}/'
    STATIC_SFTP_STORAGE_ROOT = f'/{SELCDN_STATIC_BIN}/'
    STATIC_SFTP_STORAGE_HOST = 'ftp.selcdn.ru'
    STATIC_SFTP_STORAGE_PARAMS = {
        'username': SELCDN_USERNAME,
        'password': SELCDN_PASSWORD,
    }
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_dist')
    STATIC_URL = '/static/'


#################################################################
# Media settings
#
# -- Environment variables:
# * MEDIA_PROVIDER (opt.), 'selcdn' or 'local'
#
# If MEDIA_PROVIDER == 'selcdn', then we need the following variables:
# * SELCDN_HTTP_HOST - e.g. 239120.selcdn.ru (without https:// or slashes)
# * SELCDN_USERNAME
# * SELCDN_PASSWORD
# * SELCDN_MEDIA_PUBLIC_BIN (!! without slashes)
# * SELCDN_MEDIA_PRIVATE_BIN (!! without slashes)
#################################################################
if os.environ.get('MEDIA_PROVIDER', '') == 'selcdn':
    SELCDN_HTTP_HOST = os.environ['SELCDN_HTTP_HOST']
    SELCDN_USERNAME = os.environ['SELCDN_USERNAME']
    SELCDN_PASSWORD = os.environ['SELCDN_PASSWORD']
    SELCDN_MEDIA_PUBLIC_BIN = os.environ['SELCDN_MEDIA_PUBLIC_BIN']
    SELCDN_MEDIA_PRIVATE_BIN = os.environ['SELCDN_MEDIA_PRIVATE_BIN']

    USE_LOCAL_MEDIA = False
    MEDIA_URL = f'https://{SELCDN_HTTP_HOST}/'
    DEFAULT_FILE_STORAGE = 'storages.backends.sftpstorage.SFTPStorage'
    SFTP_STORAGE_HOST = 'ftp.selcdn.ru'
    SFTP_STORAGE_ROOT = '/'
    SFTP_STORAGE_PARAMS = {
        'username': SELCDN_USERNAME,
        'password': SELCDN_PASSWORD,
    }
    MEDIA_PUBLIC_ROOT = f'/{SELCDN_MEDIA_PUBLIC_BIN}/'
    MEDIA_PRIVATE_ROOT = f'/{SELCDN_MEDIA_PRIVATE_BIN}/'
else:
    USE_LOCAL_MEDIA = True
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    MEDIA_PUBLIC_ROOT = 'public/'
    MEDIA_PRIVATE_ROOT = 'private/'


#################################################################
# Email service settings
#
# -- Environment variables:
# * EMAIL_DOMAIN (opt.)
# * EMAIL_FROM (opt.), e.g. 'support@x.y.z'
# * EMAIL_PROVIDER (opt.), e.g. 'mailgun' or 'local'
# * EMAIL_FROM_SERVER (opt., if provider is mailgun)
# * MAILGUN_TOKEN
# * MAILGUN_API_URL (opt., by default - euro domain)
#################################################################
EMAIL_DOMAIN = os.environ.get('EMAIL_DOMAIN', 'mail.localhost')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_FROM', f'support@{EMAIL_DOMAIN}')

if os.environ.get('EMAIL_PROVIDER', '') == 'mailgun':
    EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
    SERVER_EMAIL = os.environ.get('SERVER_EMAIL_FROM', f'server@{EMAIL_DOMAIN}')

    ANYMAIL = {
        "MAILGUN_API_KEY": os.environ['MAILGUN_TOKEN'],
        "MAILGUN_SENDER_DOMAIN": EMAIL_DOMAIN,
        "MAILGUN_API_URL": os.environ.get(
            'MAILGUN_API_URL', "https://api.eu.mailgun.net/v3")
    }
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
