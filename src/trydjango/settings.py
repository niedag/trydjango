"""
Django settings for trydjango project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os, ssl
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--6w4pa7o!v8@dg)hp(4x!6y#4$ia)v-l%9=!m7$b9(s*(8d9*6'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # turn to FALSE when brought into a live server or live production

ALLOWED_HOSTS = [
    "beetle-frank-supposedly.ngrok-free.app",
    "127.0.0.1",
    "http://localhost:8000/"
    'localhost'
]


# Application definition
# Cornerstone of Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # END OF DEFAULT DJANGO APPS
    'django_extensions',  # Required to run ssl server

    # Facebook authentication / All Auth required apps
    #  https://docs.allauth.org/en/latest/installation/quickstart.html for list of all possible providers
    #'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    'facebook_login',
    # my apps!
    'products',
    'pages',
    'facetest',
    'Blog',
    'accounts',  # Handles Django account signup


    'vue_app.apps.VueAppConfig',  #
    # create an app using python manage.py startapp [name]
    # then add it to this installed_apps section it !
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # This is about request and how requests are handled, how security is handled
    # Lots of default security features

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

    # Required middleware for Allauth package
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'trydjango.urls'  # how to route any given URL

TEMPLATES = [  # the html page that gets rendered in Django
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],     # In order to be OS independent
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
# This is how the server works
WSGI_APPLICATION = 'trydjango.wsgi.application'

# Django maps to databases really well.. docs has more info
# Automatically has a sqlite3 database
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# connection_string = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
# parameters = {pair.split('=')[0]: pair.split('=')[1] for pair in connection_string.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    #   'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': parameters['dbname'],
    #     'USER': parameters['user'],
    #     'PASSWORD': parameters['password'],
    #     'HOST': parameters['host'],
    # }

}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Defines where static files are stored
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Azure Cloud Setup - unsure about whitenoise still
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Redirects for Login/Logout!!
LOGIN_URL = 'accounts/login'
LOGIN_REDIRECT_URL = "home"
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"

# All Auth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
SITE_ID = 1

# SMTP Server for sending password reset emails
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" # Only good for local development - need to configure a
EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

# `allauth` specific authentication methods, such as login by email
AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'django.contrib.auth.backends.ModelBackend',  # Needed to login by username in Django admin, regardless of 'allauth'
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIAL_AUTH_FACEBOOK_KEY = "1506824033451537"
SOCIAL_AUTH_FACEBOOK_SECRET = "e0a58b1074b2237e90a152a1f4c156d0"

# All auth
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Required for All Auth
SOCIALACCOUNT_PROVIDERS = {'google': {}, 'twitter': {},
                           'facebook':
                                {'METHOD': 'oauth2',
                                 'SCOPE': ['email', 'public_profile', 'user_friends'],
                                 'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
                                 'FIELDS': [
                                     'id',
                                     'email',
                                     'name',
                                     'first_name',
                                     'last_name',
                                     'verified',
                                     'locale',
                                     'timezone',
                                     'link',
                                     'gender',
                                     'updated_time'],
                                 'EXCHANGE_TOKEN': True,
                                 'LOCALE_FUNC': lambda request: 'kr_KR',
                                 'VERIFIED_EMAIL': False,
                                 'VERSION': 'v2.4'}}

SECURE_SSL_REDIRECT = True  # Redirect HTTP requests to HTTPS
SESSION_COOKIE_SECURE = True  # Use secure cookies over HTTPS

# To locate certificate and key files if you don't want to specify it in the command
SECURE_SSL_CERT = 'C:/Users/ed/cert.pem'
SECURE_SSL_KEY = 'C:/Users/ed/key.pem'

# Required for SSL context loaded in Django uses the correct method and correct certificate and key
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(SECURE_SSL_CERT, keyfile=SECURE_SSL_KEY)
