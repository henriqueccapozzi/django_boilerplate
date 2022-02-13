from django.http import JsonResponse
from django.core import serializers

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework import permissions


from .models import Reservation
from .serializers import ReservationSerializer


@login_required
def reservations_view(request):
    ctx = {serializers.serialize("json", Reservation.objects.filter(user=request.user))}
    return JsonResponse({"msg": "This is the reservations list page"})


def reservations_add_view(request):
    return JsonResponse({"msg": "This is the reservations ADD page"})


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by("id")
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
