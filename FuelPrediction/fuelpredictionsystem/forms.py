from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	city = forms.CharField(required=True)
	state = forms.CharField(required=True)
	phone = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email", "phone","city", "state", "password1", "password2"]

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']
		user.phone = self.cleaned_data['phone']
		user.city = self.cleaned_data["city"]
		user.state = self.cleaned_data["state"]

		if commit:
			user.save()
		return user


class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'password')



