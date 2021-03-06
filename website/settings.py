"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import environ

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, 'suitable-for-development-only'),
)

DEBUG = env("DEBUG")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

if DEBUG:
    ALLOWED_HOSTS = [
        'minigigscyclingteam.local',
        'www.minigigscyclingteam.nl',
        'minigigscyclingteam.nl',
    ]
else:
    ALLOWED_HOSTS = [
        'www.minigigscyclingteam.nl',
        'minigigscyclingteam.nl',
    ]

# Application definition

INSTALLED_APPS = [
    'website.home',
    'website.photos',
    'website.users',
    'website.userprofile',
    'website.utils.form',

    # Plugins
    'django_simple_bulma',
    'sekizai',
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["website/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "sekizai.context_processors.sekizai",
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': env.db()
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Login-related settings

LOGIN_URL = '/gebruikers/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'nl'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'website', 'static')]
STATIC_ROOT = os.getenv('STATIC_ROOT', '/app/staticfiles')

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django_simple_bulma.finders.SimpleBulmaFinder',
]

MEDIA_ROOT = os.getenv('MEDIA_ROOT', '/app/mediafiles')
MEDIA_URL = '/media/'

BULMA_SETTINGS = {
    "variables": {
        "green": "#21c65c",  # Accessibility: Better contrast with the light text
        "primary": '#008cb6',
        "link": "$primary",
        "warning": "hsl(348, 100%, 61%)",

        "dimensions": "16 24 32 48 64 96 128 256 512",  # Possible image dimensions
        "navbar-height": "5rem",
        "navbar-item-img-max-height": "2.5rem",
    }
}

# Custom user model
AUTH_USER_MODEL = "users.User"

# Form Widget Templates
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
