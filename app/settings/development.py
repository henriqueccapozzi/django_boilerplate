from .base import *

DEBUG = True

DEPLOY_URL = os.environ.get("DEPLOY_URL", "")
ALLOWED_HOSTS = ["localhost", "127.0.0.1", DEPLOY_URL]


# Config for django debug tollbar
INTERNAL_IPS = ["127.0.0.1"]
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
# END Config for django debug tollbar


ACCOUNT_EMAIL_VERIFICATION = "none"

AUTH_PASSWORD_VALIDATORS = []

CORS_ALLOW_ALL_ORIGINS = True


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / ".." / "static",
]

STATIC_ROOT = BASE_DIR / ".." / "staticfiles"
