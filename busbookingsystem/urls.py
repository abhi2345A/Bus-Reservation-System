from django.contrib import admin
from django.urls import path
from selection import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('home/', views.home,name='home'),
    path('closedseats/',views.ShowClosedSeats,name='ShowClosedSeats'),
    path('admin/resetdetails/',views.reset,name='reset'),
    path('openseats/',views.ShowopenSeats,name='ShowopenSeats'),
    path('admin/resetdetails/clear/',views.Clear,name='Clear'),
    path('display/',views.Showtable,name='Showtable'),
    path('', views.home, name='register'),
    path('reg_form/', views.register, name='reg_form'),
    path('login/', views.user_login, name='login'),
    path('login/edit/', views.edit, name='edit'),
    path('login/select/', views.select, name='select'),
    path('logout/', views.logout_view, name='logout'),
    path('reg_form/login/edit/', views.edit, name='update'),
    path('Seat_layout/', views.Seat_layout, name='Seat_layout'),
]   
