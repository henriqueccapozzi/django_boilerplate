"""django_boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView

from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views as rest_auth_views

from .views import (
    auth_view,
    csrf_token_view,
    home_view,
    protected_view,
    UserViewSet,
    GroupViewSet,
)

from reservations.views import ReservationViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"reservations", ReservationViewSet)


favicon_static_url = staticfiles_storage.url("favicon.ico")
urlpatterns = [
    path("favicon.ico", RedirectView.as_view(url=favicon_static_url)),
    path("", home_view),
    path("api/", include(router.urls)),
    path("csrf/", csrf_token_view),
    path("auth/", auth_view),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api-token-auth/", rest_auth_views.obtain_auth_token),
    path("dashboard/", protected_view, name="dashboard"),
    path("accounts/", include("allauth.urls")),
    path("reservations/", include("reservations.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    # Django debug toolbar settings
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
