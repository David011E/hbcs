from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = [
        (0, 'Available'),
        (1, 'Booked'),
        (2, 'Canceled'),
    ]

    TIME_SLOTS = [
        ('9:00', '9:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '13:00 PM'),
        ('14:00', '14:00 PM'),
        ('15:00', '15:00 PM'),
        ('16:00', '16:00 PM'),
        ('17:00', '17:00 PM'),
        # Add more time slots as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_SLOTS)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.user}'s booking on {self.date} at {self.time} - {self.get_status_display()}"
