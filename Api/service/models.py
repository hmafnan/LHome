import datetime
from django.db import models
from django.core.validators import RegexValidator


class Booking(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=15,
                             validators=[RegexValidator(
                                 regex=r'^\+?1?\d{9,15}$',
                                 message="Expected format: '+999999999'. Up to 15 digits allowed.",
                                 code='Invalid number')])
    email = models.EmailField(max_length=254, blank=False)
    booking_time = models.DateTimeField(default=datetime.datetime.now())
    arrival_time = models.DateTimeField(blank=False)
    departure_time = models.DateTimeField(blank=False)
    note = models.TextField(max_length=500, blank=True, default='')
    title = models.CharField(max_length=100, blank=False, default='')

    def __repr__(self):
        return self.name + ' | ' + self.email
