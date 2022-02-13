from rest_framework import serializers
from .models import ReservationCapacity, Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        depth = 1


class ReservationCapacitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReservationCapacity
        fields = "__all__"
