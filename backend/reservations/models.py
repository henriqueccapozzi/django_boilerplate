from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings

from django.core.exceptions import ValidationError

from .constants import (
    DEFAULT_MAX_USER_SIMULTANEOUS_RESERVATIONS,
    USER_MAX_EXECUTION_FIELD_NAME,
)


MAX_MILI_CPU_ALLOWED = 500
MAX_MB_MEM_ALLOWED = 512
MAX_RESERVATION_DURATION_IN_SECONDS = 3600


class ReservationStatus(models.TextChoices):
    SCHEDULED = "S", "Scheduled"
    ACTIVE = "A", "Active"
    DONE = "D", "Done"


# Create your models here.
class ReservationLimits(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    limit = models.PositiveIntegerField(default=DEFAULT_MAX_USER_SIMULTANEOUS_RESERVATIONS)

    def __str__(self) -> str:
        return f"{self.user} - limit {self.limit}"


class Reservation(models.Model):
    # Desired datetime UTC
    # Needed capacity
    # user
    # status (active, scheduled, done)
    # provision_job_id
    needed_capacity = models.ForeignKey("ReservationCapacity", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=ReservationStatus.choices,
        default=ReservationStatus.SCHEDULED,
    )
    provision_job_id = models.UUIDField(blank=True, null=True)

    start_time = models.DateTimeField()
    duration_in_seconds = models.PositiveIntegerField(
        default=MAX_RESERVATION_DURATION_IN_SECONDS,
        validators=[MaxValueValidator(MAX_RESERVATION_DURATION_IN_SECONDS)],
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.get_status_display()} - start_time: {self.start_time}"

    def save(self, *args, **kwargs):
        qs = Reservation.objects.filter(
            user=self.user, status__in=[ReservationStatus.ACTIVE, ReservationStatus.SCHEDULED]
        ).exclude(id=self.id)
        if qs.count() >= DEFAULT_MAX_USER_SIMULTANEOUS_RESERVATIONS:
            return
        else:
            super().save(*args, **kwargs)


class ReservationCapacity(models.Model):
    cpu = models.PositiveIntegerField(validators=[MaxValueValidator(MAX_MILI_CPU_ALLOWED)])
    memory = models.PositiveIntegerField(validators=[MaxValueValidator(MAX_MB_MEM_ALLOWED)])

    def __str__(self) -> str:
        return f"{self.cpu}m cpus and {self.memory}mb memory"
