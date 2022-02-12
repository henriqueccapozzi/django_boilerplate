from django.contrib import admin

from .models import Reservation, ReservationCapacity

# Register your models here.
admin.site.register(Reservation)
admin.site.register(ReservationCapacity)
