from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import backend.apps as apps
import backend.middleware as middleware
import backend.db as db
import backend.cors as cors
import backend.templates as templates
import backend.rest_framework as rest_framework
import backend.auth_password_validation as auth_password_validation

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)0@6tj-bkm!k640rg__a=tkkl-jr%nq*dc^^)6@mdg8pp$_is*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.56.1']

# Application definition

INSTALLED_APPS = apps.INSTALLED_APPS

MIDDLEWARE = middleware.MIDDLEWARE

ROOT_URLCONF = 'backend.urls'

TEMPLATES = templates.TEMPLATES

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = db.POSTGRESQL

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = auth_password_validation.AUTH_PASSWORD_VALIDATORS

AUTH_USER_MODEL = 'accounts.User'

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CORS_ALLOWED_ORIGINS = cors.CORS_ALLOWED_ORIGINS

CORS_ALLOW_ALL_ORIGINS = cors.CORS_ALLOW_ALL_ORIGINS

REST_FRAMEWORK = rest_framework.REST_FRAMEWORK

SIMPLE_JWT = rest_framework.SIMPLE_JWT

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
