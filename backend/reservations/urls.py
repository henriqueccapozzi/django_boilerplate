from django.urls import path

from .views import reservations_add_view, reservations_view

urlpatterns = [
    path("", reservations_view),
    path("add/", reservations_add_view),
]
