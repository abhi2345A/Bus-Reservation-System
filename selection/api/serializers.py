from rest_framework import serializers
from selection.models import Passenger,Seat,User


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['passenger_name', 'journeyfrom', 'journeyto', 'gender', 'dob', 'seat']


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['no', 'seat_type', 'vacant']

'''
class RegisterSerializer(serializers.ModelSerializer):
	#password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
	

	class Meta:
		model = User
		fields = ['username','password1','password2']
		extra_kwargs = {'username': {'required': False}}

	def save(self):
		account = User(
					#is_warden = self.validated_data['is_warden'],
					username = self.validated_data['username'],
					password1  = self.validated_data['password1'],
					password2 = self.validated_data['password2']
			)
		
		
		

		if password1!=password2:
			raise serializers.ValidationError({'password':'Passwords must match'})
		account.set_password(password1)
		account.save()
		return account

'''