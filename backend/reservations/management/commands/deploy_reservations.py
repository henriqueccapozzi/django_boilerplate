from datetime import timedelta
from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.utils import timezone

from reservations.models import Reservation


DEPLOY_WINDOW_IN_MINUTES = 180


def deploy_reservation(reservation_obj):
    print("  Connect to cloud instance")
    print("  Clone the repository with correct tag")
    print("  Create/start the necessary containers")
    print("  schedule a cleanup function")
    pass


def print_header(command_instance: BaseCommand):
    command_instance.stdout.write(f"Current server datetime is {timezone.now()}\n")


class Command(BaseCommand):
    help = "Get reservations in the future and deploy then"

    def handle(self, *args: Any, **kwargs: Any) -> Optional[str]:
        qs = Reservation.objects.filter(
            start_time__gte=timezone.now(),
            start_time__lt=(timezone.now() + timedelta(minutes=DEPLOY_WINDOW_IN_MINUTES)),
        )
        print_header(self)
        for reservation in qs:
            self.stdout.write(f" deploying reservervation: {reservation}\n")
            deploy_reservation(reservation)
