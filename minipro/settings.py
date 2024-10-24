"""
Django settings for minipro project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from mongoengine import connect
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@y+)^pnqv)*gq$$l5pa2u(ci1m&@%y&z&uc9+d58*bc!ehtd(='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['django-project-z8gp.onrender.com', 'localhost', '127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Token valid for 60 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),     # Refresh token valid for 1 day
    'ROTATE_REFRESH_TOKENS': True,  # Refresh token can generate new refresh tokens
}



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]


ROOT_URLCONF = 'minipro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'minipro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'myDB',
#         'CLIENT': {
#             'host': 'mongodb+srv://hulashkumar:hulashkr7@cluster0.ruix7.mongodb.net/myDB?retryWrites=true&w=majority&appName=Cluster0',
#             'username': 'hulashkumar',
#             'password': 'hulashkr7',
#             'authMechanism': 'SCRAM-SHA-1',
#         }
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'djangoDB',  # Replace with your MongoDB database name
#         'CLIENT': {
#             'host': 'mongodb+srv://Sahil_Salmania:Sahilkhan786@cluster0.hrxdv.mongodb.net/djangoDB?retryWrites=true&w=majority&appName=Cluster0',
#             'username': 'Sahil_Salmania',  # Your MongoDB Atlas username
#             'password': 'Sahilkhan786',  # Your MongoDB Atlas password
#             'authMechanism': 'SCRAM-SHA-1',
#         }
#     }
# }

connect(
    db='myDB',
    username='Sahil_Salmania',
    password='Sahilkhan786',
    host='mongodb+srv://Sahil_Salmania:Sahilkhan786@cluster0.hrxdv.mongodb.net/myDB?retryWrites=true&w=majority&appName=Cluster0',
    authentication_mechanism='SCRAM-SHA-1'
)

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://192.168.249.101:8000",  # Your actual IP address
    "https://django-project-z8gp.onrender.com",
    "http://localhost:3000",
]


APPEND_SLASH = False