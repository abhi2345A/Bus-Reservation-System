from django.test import TestCase, Client
from django.urls import reverse
from selection.models import User, Passenger , Room
import json 
import unittest
from django.contrib.auth import get_user_model

class TestViews(TestCase):

	def test_login_GET(self):
		client = Client()

		response = client.get(reverse('login'))

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'login.html')


	def test_register_GET(self):
		client = Client()

		response = client.get(reverse('register'))

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'base.html')


	def test_home_GET(self):
		client = Client()

		response = client.get(reverse('home'))

		self.assertEquals(response.status_code,200)
		self.assertTemplateUsed(response,'home.html')

	def Seat_layout(self):
 		client = Client()

 		response = client.get(reverse('Seat_layout'))

 		self.assertEquals(response.status_code,200)
 		self.assertTemplateUsed(response,'Seat_layout.html')







