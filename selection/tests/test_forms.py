from django.test import TestCase
from selection.forms import UserForm, LoginForm, RegistrationForm

class TestForms(TestCase):

	def test_UserForm(self):
		form = UserForm(data={
			'username':'CR7',
			'password1':'Ronaldo1234!',
			'password2':'Ronaldo1234!'
			})

		self.assertTrue(form.is_valid())


	def test_LoginForm(self):
		form = LoginForm(data={
			'username':'CR7',
			'password':'Ronaldo1234!'
			})

		self.assertTrue(form.is_valid())


	def test_RegistrationForm(self):
		form = RegistrationForm(data={
			'passenger_name':'ronaldo',
            'journeyfrom':'Lucknow',
            'journeyto':'Bengaluru',
            'dob':'1985-12-12',
            'gender':'M',
			})

		self.assertTrue(form.is_valid())
