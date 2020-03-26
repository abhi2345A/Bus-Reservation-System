from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selection.models import User, Passenger,Room
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time,os

class TestProject(StaticLiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(ChromeDriverManager().install())

	def tearDown(self):
		self.browser.close()


	def test_display(self):
		self.browser.get(self.live_server_url)
		time.sleep(3)
		add_url = self.live_server_url+reverse('login')
		self.browser.find_element_by_xpath('//a[contains(@href,"Seat_layout")]').click()
		time.sleep(5)
		self.browser.find_element_by_xpath('//a[contains(@href,"/")]').click()
		time.sleep(5)
		self.assertEquals(1,1)



	def test_login_function(self):
		os.system('cls||clear')
		self.browser.get(self.live_server_url)
		add_url = self.live_server_url+reverse('login')
		self.browser.find_element_by_xpath('//a[contains(@href,"login")]').click()
		self.assertEquals(add_url,self.live_server_url+reverse('login'))


	def test_register_function(self):
		os.system('cls||clear')
		self.browser.get(self.live_server_url)
		add_url = self.live_server_url+reverse('reg_form')
		self.browser.find_element_by_xpath('//a[contains(@href,"reg_form")]').click()
		self.assertEquals(add_url,self.live_server_url+reverse('reg_form'))
