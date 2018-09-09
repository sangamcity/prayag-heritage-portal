"""
Django settings for prayag project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from unipath import Path
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']
# GITHUB_SECRET_KEY = config('GITHUB_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER='deepakbharti@mnnit.ac.in'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = 587

'''
If using gmail, you will need to
unlock Captcha to enable Django 
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #modules installed
    'crispy_forms',
    'rosetta',
    #custom apps
    'TourismPlaces',
    'Users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prayag.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates'),
                BASE_DIR.child('templates','templates'),
                ],
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

WSGI_APPLICATION = 'prayag.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# print(DB_PASS)
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
else:
    # DB_PASS = os.environ['prayag_PASS']
    # # DATABASES = {
    # #     'default': {
    # #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    # #         'NAME': 'prayag_db',
    # #         'USER': 'prayag_user',
    # #         'PASSWORD': DB_PASS,
    # #         'HOST': 'localhost',
    # #         'PORT': '',
    # #     }
    # # }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', 'English'),
    ('hi', 'Hindi'),
)

LOCALE_PATHS = (BASE_DIR.child('locale'), )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
# static_root is the server outside our project wher e static files are sent to store

STATICFILES_DIRS = (
    BASE_DIR.child('static'),
    #'/var/www/static/',
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_files')

#Crispy forms tags settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'


SITE_ID = 1
# added on 15_jan
LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
 
ALLOWED_SIGNUP_DOMAINS = ['*']
 
FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644

#added to host on heroku
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

import netifaces

# Find out what the IP addresses are at run time
# This is necessary because otherwise Gunicorn will reject the connections
def ip_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list

# Discover our IP address
ALLOWED_HOSTS += ip_addresses()
