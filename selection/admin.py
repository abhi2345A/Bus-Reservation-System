from django.contrib import admin
from .models import Student, Room, User, Warden


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'student_name',
        'father_name',
        'gender',
        'dob',
        'room',
        'room_allotted']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['no', 'name', 'room_type', 'vacant',]



@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['is_warden']


@admin.register(Warden)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
