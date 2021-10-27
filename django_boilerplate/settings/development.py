from .base import *

DEBUG = True

DEPLOY_URL = os.environ.get("DEPLOY_URL", "")
ALLOWED_HOSTS += ["localhost", "127.0.0.1", DEPLOY_URL]

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ACCOUNT_EMAIL_VERIFICATION = "none"

AUTH_PASSWORD_VALIDATORS = []

CORS_ALLOW_ALL_ORIGINS = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / ".." / "static",
]

STATIC_ROOT = BASE_DIR / ".." / "staticfiles"
