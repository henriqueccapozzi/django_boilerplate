from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY_FROM_ENV = "DJANGO_SECRET_KEY" in os.environ
if not SECRET_KEY_FROM_ENV:
    raise RuntimeError(
        "To start django with production conf the environment variable DJANGO_SECRET_KEY must be set"
    )

DEBUG = False

DEPLOY_URL = os.environ.get("DEPLOY_URL", "")

# For heroku deploy - according to
# https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Security recomendations based on ./manage.py check --deploy
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 1
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Production ORIGIN
ALLOWED_HOSTS = [DEPLOY_URL]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
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

CORS_ALLOWED_ORIGINS = [
    f"https://{DEPLOY_URL.split('.')[:-1]}.com",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / ".." / "static",
]

STATIC_ROOT = BASE_DIR / ".." / "staticfiles"
