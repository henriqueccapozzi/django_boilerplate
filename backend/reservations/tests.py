from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone

from django.test import TestCase

from .constants import DEFAULT_MAX_USER_SIMULTANEOUS_RESERVATIONS as MAX_RESERVATIONS

from .models import Reservation, ReservationCapacity, ReservationStatus, ReservationLimits

User = get_user_model()


def ReservationFactory(user, capacity, timedelta_obj):
    return Reservation.objects.create(
        needed_capacity=capacity,
        user=user,
        status=ReservationStatus.SCHEDULED,
        start_time=timezone.now() + timedelta_obj,
    )


# Create your tests here.
class ReservationTestCase(TestCase):
    def setUp(self) -> None:
        self.user_1 = User.objects.create(username="user_1", password="12345678", email="")
        self.user_2 = User.objects.create(username="user_2", password="12345678", email="")
        self.capacities = {
            "small": ReservationCapacity.objects.create(cpu=200, memory=200),
        }
        ReservationLimits.objects.create(user=self.user_1, limit=1)
        ReservationLimits.objects.create(user=self.user_2, limit=2)

    def test_user_can_reserve_when_he_already_have_an_ended_reservation(self):
        r1 = Reservation.objects.create(
            user=self.user_1,
            needed_capacity=self.capacities["small"],
            status=ReservationStatus.DONE,
            start_time=timezone.now() - timedelta(days=3),
        )
        r2 = ReservationFactory(self.user_1, self.capacities["small"], timedelta(days=3))
        self.assertEqual(
            Reservation.objects.filter(user=self.user_1).count(),
            2,
        )

    def test_reservation_only_creates_if_current_user_is_bellow_allowed_limit(self):
        r1 = ReservationFactory(self.user_1, self.capacities["small"], timedelta(days=3))
        r2 = ReservationFactory(self.user_1, self.capacities["small"], timedelta(days=3))

        self.assertEqual(
            Reservation.objects.filter(user=self.user_1).count(),
            MAX_RESERVATIONS,
            f"A user can't create more than the allowed simultaneous active reservations {MAX_RESERVATIONS}",
        )
