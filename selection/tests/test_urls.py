from django.test import SimpleTestCase,TestCase
from django.urls import reverse, resolve
from django.test.client import RequestFactory
from selection.views import user_login,home,register,logout_view,Seat_layout
from selection.views import ShowClosedSeats,Showtable,ShowopenSeats
from django.contrib.auth.models import User
from django.test.client import Client
from django.contrib.auth import get_user_model
import unittest


class TestUrls(SimpleTestCase):
	def test_login_url_is_resolved(self):
		url = reverse('login')
		self.assertEquals(resolve(url).func,user_login)

	def test_home_url_is_resolved(self):
		url = reverse('home')
		self.assertEquals(resolve(url).func,home)

	def test_register_url_is_resolved(self):
		url = reverse('reg_form')
		self.assertEquals(resolve(url).func,register)

	def test_logout_view_url_is_resolved(self):
		url = reverse('logout')
		self.assertEquals(resolve(url).func,logout_view)

	def test_Seat_layout_url_is_resolved(self):
		url = reverse('Seat_layout')
		self.assertEquals(resolve(url).func,Seat_layout)

	

'''
class TestUrls1(unittest.TestCase):


	def create_test_user(self):
		User = get_user_model()
		self.user = User.objects.create_user('Zain', 'Zain1234!', 'Zain1234!')
		return ['Zain','Zain1234!']


	def delete_test_user(self):
		self.user.delete()



	def test_Showtable_url(self):
		self.client = Client()
		username,password = self.create_test_user()
		self.client.login(username=username,password=password)
		response = self.client.get(reverse('Showtable'))
		self.delete_test_user()
		self.assertEqual(response.status_code,200)


	def test_ShowClosedSeats_url(self):
		self.client = Client()
		username,password = self.create_test_user()
		self.client.login(username=username,password=password)
		response = self.client.get(reverse('ShowClosedSeats'))
		self.delete_test_user()
		self.assertEqual(response.status_code,200)

	def test_ShowopenSeats_url(self):
		self.client = Client()
		username,password = self.create_test_user()
		self.client.login(username=username,password=password)
		response = self.client.get(reverse('ShowopenSeats'))
		self.delete_test_user()
		self.assertEqual(response.status_code,200)

'''
	




