import datetime
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user


class  FuelQuoteForm(forms.Form):
	class Metal:
		model = User
		fields = ["gallons_requested", "delivery_date", "delivery_address"]

	gallons_requested = forms.DecimalField(
		help_text="Input Gallons (required)", 
		required=True, 
		max_value=1000.00, 
		min_value=0.00, 
		max_digits=6, 
		decimal_places=2)
	
	delivery_date = forms.DateField(
		help_text="Please pick a date",
		required=True,
		localize=True,
		widget=forms.DateInput(format='%m/%d/%Y', attrs={
			'class': 'form-control datetimepicker-input',
			'data-target': '#datetimepicker1'}),
		input_formats='%m/%d/%Y'
	)

	delivery_address = forms.CharField(
		help_text="Please enter your address",
		required=True)

	def clean_delivery_date(self):
		data = self.cleaned_data['delivery_date']

		# Check if a date in not in the past
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - Date must be in the future'))

		# Check if data is not the current day
		if data == datetime.data.today():
			raise ValidationError(_('Invalid date - Date must be in the future'))

		return data

	def save(self, commit=True):
		user = super(FuelQuoteForm, self).save(commit=False)
		user.gallons_requested = self.cleaned_data['gallons_requested']
		user.delivery_date = self.cleaned_data['delivery_date']
		user.delivery_address = self.cleaned_data['delivery_address']

		if commit:
			user.save()
		return user
	
