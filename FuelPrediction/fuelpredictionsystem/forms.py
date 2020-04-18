from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
# from .models import PriceModule
from .models import UserProfile



class RegisterForm(UserCreationForm):

	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ('username', 'email','password1', 'password2')

	def save(self, commit=True):
		# user = super(RegisterForm, self).save(commit=False)
		user = super().save(commit=False)
		user.email = self.cleaned_data['email']
		# user.phone = self.cleaned_data['phone']
		# user.city = self.cleaned_data["city"]
		# user.state = self.cleaned_data["state"]

		if commit:
			user.save()
		return user


class UserProfileFrom(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('fullname', 'address', 'city', 'state', 'zipcode')



class EditProfileForm(UserChangeForm):
	class Meta:
		model = UserProfile
		fields = ('fullname', 'address', 'city', 'state', 'zipcode')
		# fields = ('email', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'password')


# class EditProfileForm(UserChangeForm):
# 	class Meta:
# 		model = User
# 		fields = ('email', 'first_name', 'last_name', 'password')
# 		# fields = ('email', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'password')
		


# class  FuelQuoteForm(forms.Form):
# 	class Meta:
# 		model = User
# 		fields = ["gallons_requested", "delivery_date", "delivery_address", "location", "season"]

# 	gallons_requested = forms.IntegerField(
# 		help_text="Input Gallons (required)", 
# 		required=True, 
# 		max_value=10000, 
# 		min_value=1
# 		)
	
# 	delivery_date = forms.DateField(
# 		help_text="Please pick a date",
# 		required=True,
# 		localize=True,
# 		widget=forms.DateInput(format='%m/%d/%Y', attrs={
# 			'class': 'form-control datetimepicker-input',
# 			'data-target': '#datetimepicker1'}),
# 		input_formats='%m/%d/%Y'
# 	)

# 	delivery_address = forms.CharField(
# 		help_text="Please enter your address",
# 		required=True)

# 	location = forms.ChoiceField(widget=forms.Select(choices=STATE),
# 		help_text="Please select",
# 		required=True)

# 	season = forms.ChoiceField(widget=forms.Select(choices=RATE),
# 		help_text="Please select",
# 		required=True)

# 	def clean_delivery_date(self):
# 		data = self.cleaned_data['delivery_date']

# 		# Check if a date in not in the past
# 		if data < datetime.date.today():
# 			raise ValidationError(_('Invalid date - Date must be in the future'))

# 		# Check if data is not the current day
# 		if data == datetime.data.today():
# 			raise ValidationError(_('Invalid date - Date must be in the future'))

# 		return data

# 	def save(self, commit=True):
# 		user = super(FuelQuoteForm, self).save(commit=False)
# 		user.gallons_requested = self.cleaned_data['gallons_requested']
# 		user.delivery_date = self.cleaned_data['delivery_date']
# 		user.delivery_address = self.cleaned_data['delivery_address']
# 		user.location = self.cleaned_data['location']
# 		user.season = self.cleaned_data['season']

# 		if commit:
# 			user.save()
# 		return user


# class  FuelQuoteForm(forms.ModelForm):
#     error_css_class = 'error'
#     location = forms.ChoiceField(choices=STATE, required=True )
#     season = forms.ChoiceField(choices=SEASON, required=True )
#     class Meta:
#     	model = PriceModule
#     	fields = ["gallons_requested", "delivery_date", "delivery_address", "location", "season"]

	# def save(self, commit=True):
	# 	PriceModule = super(FuelQuoteForm, self).save(commit=False)
	# 	PriceModule.gallons_requested = self.cleaned_data['gallons_requested']
	# 	PriceModule.delivery_date = self.cleaned_data['delivery_date']
	# 	PriceModule.delivery_address = self.cleaned_data['delivery_address']
	# 	PriceModule.location = self.cleaned_data['location']
	# 	PriceModule.season = self.cleaned_data['season']

	# 	if commit:
	# 		PriceModule.save()
	# 	return PriceModule

