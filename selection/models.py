from django.db import models
from django.contrib.auth.models import AbstractUser


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
        'Room',
        blank=True,
        on_delete=models.CASCADE,
        null=True)
    seat_allotted = models.BooleanField(default=False)

    #def __str__(self):
    #    return self.enrollment_no


class Room(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="room_details")
    room_choice = [('Window Seat', 'Window Seat'), ('Middle Seat', 'Middle Seat'), ('Inner Seat', 'Inner Seat')]
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=10)
    room_type = models.CharField(choices=room_choice, max_length=30, default=None)
    vacant = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Warden(models.Model):
    user = models.OneToOneField(
        User,
        default=None,
        null=True,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

