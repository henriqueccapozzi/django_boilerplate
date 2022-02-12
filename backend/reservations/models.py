from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings

MAX_MILI_CPU_ALLOWED = 500
MAX_MB_MEM_ALLOWED = 512
MAX_RESERVATION_DURATION_IN_SECONDS = 3600


RESERVATION_STATUS_CHOICES = (
    ("S", "Scheduled"),  # Default by typle index == 0
    ("A", "Active"),
    ("D", "Done"),
)


# Create your models here.
class Reservation(models.Model):
    # Desired datetime UTC
    # Needed capacity
    # user
    # status (active, scheduled, done)
    # provision_job_id
    needed_capacity = models.OneToOneField(
        "ReservationCapacity", on_delete=models.CASCADE
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1,
        choices=RESERVATION_STATUS_CHOICES,
        default=RESERVATION_STATUS_CHOICES[0],
    )
    provision_job_id = models.UUIDField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.user} - {self.get_status_display()}"


class ReservationCapacity(models.Model):
    cpu = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_MILI_CPU_ALLOWED)]
    )
    memory = models.PositiveIntegerField(
        validators=[MaxValueValidator(MAX_MB_MEM_ALLOWED)]
    )

    def __str__(self) -> str:
        return f"{self.cpu}m cpus and {self.memory}mb memory"
