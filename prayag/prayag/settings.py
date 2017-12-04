# Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
import os 
from unipath import Path
    
 
# PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_DIR = Path(__file__).parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = '7yl&y17r&7h*#fk&wfh0%imys#^m$0+k$)l!-idm*md%w_ldcj'
   
# SECURITY WARNING: don't run with debug turned on in production!
  
# when this is false production settings will be used, if its true local settings will be used
DEBUG = True # if you set it False then the allowed host must be saved to som port like 4 7 etc or just set it to all like ['*']

ALLOWED_HOSTS = []   
     
  
ADMINS = ( 
    ('deepak','deepakbharti823@gmail.com'),
    ('sushant','sushant@gmail.com'),
    ('Suraj','deepakbharti823@gmail.com'),
    ('ritika','ritika@gmail.com'),
    ('vikas','vika@gmail.com'),
    ('samyak','samyak@gmail.com'),    
    )
        
 
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'deepakbharti823@gmail.com'
EMAIL_HOST_USER='email@gmail.com'
# EMAIL_HOST_PASSWORD = 'zwmdutnsiyyhskge'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587


''' 
If using gmail, you will need to
unlock Captcha to enable Django 
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''


# AUTH_USER_MODULE = 'authentication.Profile'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #modules installed

    #custom apps
    'TourismPlaces',
    'Users',
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
ROOT_URLCONF = 'prayag.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR.child('templates'),
                PROJECT_DIR.child('templates','templates'),
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
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': PROJECT_DIR.child('db.sqlite3'),
#     }
# } 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR.child('db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'hohos_database',
#         'USER': 'root',
#         'PASSWORD': 'kali@161ss',
#         'HOST': '139.59.69.62',
#         'PORT': '',
#     }
# }



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# LANGUAGES = (
#     ('en', 'English'),
#     ('pt-br', 'Portuguese'),
#     ('es', 'Spanish')
# )

# LOCALE_PATHS = (PROJECT_DIR.child('locale'), )



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = PROJECT_DIR.child('prayag','static_root')
# static_root is the server outside our project wher e static files are sent to store

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
    #'/var/www/static/',
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_DIR.child('prayag','media_root')

#Crispy forms tags settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'


SITE_ID = 1
# added on 15_jan
# LOGIN_URL = '/'
# LOGIN_REDIRECT_URL = '/introho/'
 
ALLOWED_SIGNUP_DOMAINS = ['*']
 
FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0o644


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
