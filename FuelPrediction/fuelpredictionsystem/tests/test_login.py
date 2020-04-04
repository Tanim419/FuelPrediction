import unittest
from django.urls import reverse, resolve
from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from fuelpredictionsystem.views import go_home_page
from mixer.backend.django import mixer
import pytest
#from FuelPrediction import fuelpredictionsystem


# class TestLogin(Testcase):

@pytest.mark.django_db
class TestLoginPage:


	def test_login(self):
		path = reverse('Home', kwargs={})
		request = RequestFactory().get(path)
		request.user = mixer.blend(User)

		response = go_home_page(request)

		assert response.status_code == 200



    	# return client.post('/login', data=dict(username=username, password=password), follow_redirects=True)

	# def test_main_page(self):
	# 	# return self.registration.post ('/login', data =  dict(username = username, password = password), follow_redirects=True)
	# 	response =self.app.get('/', follow_redirects=True)
	# 	self.assertEqual (response.status_code, 200)

