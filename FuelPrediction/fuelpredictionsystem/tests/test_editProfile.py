import unittest
#from fuelpredictionsystem import registration
from django.test import TestCase
from fuelpredictionsystem.forms import EditProfileForm
# Create your tests here.


class TestEditProfileForm(TestCase):
  
	def test_registration_form(self):
    	# test invalid data
	   #  invalid_data = {
		  # "email" : "",
		  # "first_name" : "",
		  # "last_name" : ""

	   #  }
	   #  form = EditProfileForm(data=invalid_data)
	   #  form.is_valid()
	   #  self.assertTrue(form.errors)

	    #test valid data
	    valid_data = {
		  "email" : "entima@gmail.com",
		  "first_name" : "Imtiaz",
		  "last_name" : "Nur"
	    }
	    form = EditProfileForm(data=valid_data)
	    form.is_valid()
	    self.assertFalse(form.errors)



