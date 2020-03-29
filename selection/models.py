from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


class User(AbstractUser):
    is_warden = models.BooleanField(default=False)





class Passenger(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    passenger_name = models.CharField(max_length=200, null=True)
    journeyfrom = models.CharField(max_length=200, null=True)
    journeyto = models.CharField(max_length=200, null=True)
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    seat = models.OneToOneField(
        'Seat',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    seat_allotted = models.BooleanField(default=True)



    #def __str__(self):
    #    return self.enrollment_no


class Seat(models.Model):
    seat_choice = [('Window Seat', 'Window Seat'), ('Inner Seat', 'Inner Seat')]
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=10)
    seat_type = models.CharField(choices=seat_choice, max_length=30, default=None)
    vacant = models.BooleanField(default=False)

    def __str__(self):
        return str(self.no)
        


