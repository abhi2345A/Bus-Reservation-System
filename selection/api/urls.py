from django.urls import path
from selection.api.views import api_passenger_view,api_seat_view,api_reset
from selection.api.views import api_closedtickets,api_opentickets

app_name = 'selection'
urlpatterns = [ 
	path('pdetail/',api_passenger_view,name='pdetail'),
	path('sdetail/',api_seat_view,name='sdetail'),
	#path('registernew/',register_view,name='registernew'),
	path('apireset/',api_reset,name='apireset'),
	path('apiclosed/',api_closedtickets,name='apiclosed'),
	path('apiopen/',api_opentickets,name='apiopen'),
	#path('<slug>',api_login,name='apilogin')
]