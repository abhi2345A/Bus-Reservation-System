from django.contrib import admin
from .models import Passenger, Seat, User


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'passenger_name',
        'journeyfrom',
        'journeyto',
        'dob',
        'gender',
        'seat',
        'seat_allotted']


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['no', 'name', 'seat_type', 'vacant',]



@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['is_warden']

