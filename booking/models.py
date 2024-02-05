from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = [
        (0, 'Available'),
        (1, 'Booked'),
        (2, 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.user}'s booking on {self.date} at {self.time} - {self.get_status_display()}"
