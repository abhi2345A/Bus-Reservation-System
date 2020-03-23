from django.contrib import admin
from django.urls import path
from selection import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('closedseats/',views.ShowClosedSeats,name='ShowClosedSeats'),
    path('openseats/',views.ShowopenSeats,name='ShowopenSeats'),
    path('display/',views.Showtable,name='Showtable'),
    path('', views.home, name='register'),
    path('reg_form/', views.register, name='reg_form'),
    path('login/', views.user_login, name='login'),
    path('warden_login/', views.warden_login, name='warden_login'),
    #path('hostels/<slug:hostel_name>/', views.hostel_detail_view, name='hostel'),
    path('login/edit/', views.edit, name='edit'),
    path('login/select/', views.select, name='select'),
    path('logout/', views.logout_view, name='logout'),
    path('reg_form/login/edit/', views.edit, name='update'),
    path('BH5_Floor4/', views.BH5_Floor4, name='BH5_Floor4'),
]
