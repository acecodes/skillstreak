from django.test import TestCase
from selenium import webdriver

class FuncTest(TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_front_page_up(self):
		driver = self.driver
		driver.get("http://127.0.0.1:8100")
		self.assertIn("SkillStreak", driver.title)

	def test_api_up(self):
		driver = self.driver
		driver.get("http://127.0.0.1:8100/api")
		self.assertIn("Django REST", driver.title)
		
	def tearDown(self):
		self.driver.close()


