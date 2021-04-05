from dotenv import load_dotenv
from pathlib import Path
from decouple import config, Csv
import os
import dj-database-url

load_dotenv()
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "dashboard",
    "eventreg",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oschub.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "oschub.wsgi.application"

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": config("GOOGLE_CLIENT_ID"),
            "secret": config("GOOGLE_SECRET_KEY"),
            "key": "",
        },
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIR = (
        os.path.join(BASE_DIR, 'static'),
    )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SITE_ID = 1
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_LOGOUT_REDIRECT_URL = "/dashboard/"
LOGIN_REDIRECT_URL = "/dashboard/"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('USER_EMAIL')
EMAIL_HOST_PASSWORD = config('USER_PASS')
