"""
Django settings for trydjango project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#C:\Users\ed\Dev\trydjango\src

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--6w4pa7o!v8@dg)hp(4x!6y#4$ia)v-l%9=!m7$b9(s*(8d9*6'

# FACEBOOK API CREDENCIALS
FACEBOOK_APP_ID = '838106777784601'
FACEBOOK_APP_SECRET = 'f18ffa5fd6ea0a2f2e5e8168b1b7f81d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # turn to FALSE when brought into a live server or live production

ALLOWED_HOSTS = []


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
    # This is where your apps or products core to your website.
    # Pieces of your Django project

    # my apps!
    'products',
    'pages',
    'facetest',
    # create an app using python manage.py startapp [name]
    # then add it to this installed_apps section!
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
    #'facebook.middleware.SignedRequestMiddleware',
    #'facebook.middleware.AppRequestMiddleware',
]

ROOT_URLCONF = 'trydjango.urls' #how to route any given URL

TEMPLATES = [ # the html page that gets rendered in Django
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],                                                     # Needs to be OS independent
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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
