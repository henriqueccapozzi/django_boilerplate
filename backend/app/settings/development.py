from .base import *

DEBUG = True

DEPLOY_URL = os.environ.get("DEPLOY_URL", "")
ALLOWED_HOSTS = ["*", "127.0.0.1", DEPLOY_URL]


# Config for django debug tollbar

# Settings for docker environment
# 2021-12-11
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips
# Simple way to check if is inside a docker container
import os

if os.path.exists("/.dockerenv"):
    import socket

    print("Django is running inside a docker container")
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1"]
else:
    INTERNAL_IPS = ["127.0.0.1"]

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE = (
    MIDDLEWARE[:1]
    + ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    + MIDDLEWARE[1:]
)

# END Config for django debug tollbar


ACCOUNT_EMAIL_VERIFICATION = "none"

AUTH_PASSWORD_VALIDATORS = []

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / ".." / "static",
    BASE_DIR / ".." / "frontend" / "out",
    BASE_DIR / ".." / "frontend" / "out" / "_next" / "static",
]

STATIC_ROOT = BASE_DIR / ".." / "staticfiles"


REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append(
    "rest_framework.authentication.SessionAuthentication"
)

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = ["http://localhost:8080"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

LOGIN_REDIRECT_URL = "/dashboard/"
