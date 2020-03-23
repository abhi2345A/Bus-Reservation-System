from django.contrib import admin
from .models import Passenger, Room, User, Warden


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


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['no', 'name', 'room_type', 'vacant',]



@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['is_warden']


@admin.register(Warden)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
