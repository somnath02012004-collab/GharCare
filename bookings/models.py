from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):

    SERVICE_CHOICES = [
        ('AC Repair', 'AC Repair'),
        ('Plumbing', 'Plumbing'),
        ('Cleaning', 'Cleaning'),
        ('Beauty', 'Beauty'),
        ('Spa', 'Spa'),
        ('Hair Care', 'Hair Care'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )

    booking_date = models.DateField()

    booking_time = models.TimeField()

    address = models.TextField()

    phone = models.CharField(max_length=15)

    notes = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service}"