from django.contrib.auth.models import User
from django.db import models

class Turf(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.turf.name} on {self.date}"
