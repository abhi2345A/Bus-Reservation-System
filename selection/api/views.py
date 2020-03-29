from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from selection.models import Passenger,Seat
from selection.api.serializers import PassengerSerializer,SeatSerializer
from django.http import JsonResponse
from django.http import HttpResponse
from selection.forms import UserForm, RegistrationForm, LoginForm, SelectionForm

'''
@api_view(['GET',])
def api_passenger_view(viewsets.ModelViewSet):
	try:
		passenger = Passenger.objects.all()
	except Passenger.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND) 
	except Passenger.MultipleObjectsReturned:
		passenger = Passenger.objects.get(passenger_name='Joker')

	#if request.method == "GET":
	serializer = PassengerSerializer(passenger,many=True)
	return Response(serializer.data)
'''
@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def api_passenger_view(request):
	passenger = Passenger.objects.all()
	serializer = PassengerSerializer(passenger,many=True)
	return Response(serializer.data) 



@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def api_seat_view(request):
	seat = Seat.objects.all()
	serializer = SeatSerializer(seat,many=True)
	return JsonResponse(serializer.data, safe=False)



@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def api_reset(request):
	default = True
	for seat in Seat.objects.all():
		seat.vacant = default
		seat.save()
	for passenger in Passenger.objects.all():
		passenger.seat = None
		passenger.seat_allotted = False
		passenger.save()
	data={}
	data['response'] = "All The Seat Tickets Have Been Reset Successfully!"
	return JsonResponse(data, safe=False)



@api_view(['GET',])
def api_closedtickets(request):
	data = {}
	data['response'] = 'Seat tickets that are closed now!'
	i=1
	for seat in Seat.objects.all():
		e = {}
		if not seat.vacant:
			e['no'] = seat.no
			e['Type'] = seat.seat_type
			data[i]=e 
			i+=1
	return JsonResponse(data, safe=False)



@api_view(['GET',])
def api_opentickets(request):
	data = {}
	data['response'] = 'Seat tickets that are currently open'
	i=1
	for seat in Seat.objects.all():
		e = {}
		if  seat.vacant:
			e['no'] = seat.no
			e['Type'] = seat.seat_type
			data[i]=e 
			i+=1
	return JsonResponse(data, safe=False)


'''

@api_view(['POST',])
def api_login(request,slug):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(
                request,
                username=cd['username'],
                password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					try:
						passenger = request.user.passenger
						data = {}
						data['user'] = 'found'
						data['passenger_name'] = passenger.passenger_name
						data['Journeyfrom'] = passenger.Journeyfrom
						data['Journeyto'] = passenger.Journeyto
						data['dob'] = passenger.dob
						data['gender'] = passenger.gender
						data['seat'] = passenger.seat
						return JsonResponse(data, safe=False)	
					except Exception as e:
						data = {}
						data['status']='status.HTTP_404_NOT_FOUND'
						return Response(data,status=status.HTTP_404_NOT_FOUND)
				else:
					return HttpResponse('Disabled account')
			else:
				data = {}
				data['status']='status.HTTP_404_NOT_FOUND'
				return Response(data,status=status.HTTP_404_NOT_FOUND)
		else:
			data = {}
			data['status']='status.HTTP_404_NOT_FOUND'
			return Response(data,status=status.HTTP_404_NOT_FOUND)
	else:
		data = {}
		data['status']='status.HTTP_404_BAD_REQUEST'
		return Response(data,status=status.HTTP_404_BAD_REQUEST)



@api_view(['POST',])
def register_view(request):

	if request.method == 'POST':
		serializer = RegisterSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = "Successfully Registered a New User!"
			data['username'] = account.username
		else:
			return HttpResponse('Its not working!')
			data = serializer.errors
		return Response(data)
'''