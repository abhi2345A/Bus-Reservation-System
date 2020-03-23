from django.contrib.auth.forms import UserCreationForm
from .models import Passenger, User
from django import forms


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': 'same as your roll no.',
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = [
            'passenger_name',
            'journeyfrom',
            'journeyto',
            'dob',
            'gender']


class SelectionForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['seat']

