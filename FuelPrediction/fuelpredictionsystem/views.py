#from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile



def index(request):
	#return HttpResponse("Tech with tim!")
	return render(request, 'fuelpredictionsystem/home.html')

def home(request):
	 return render(request, 'fuelpredictionsystem/home.html')
	
# def clientProfile(request):
# 	return render(request, 'fuelpredictionsystem/clientProfile.html')

def fuelQuoteForm(request):
	return render(request, 'fuelpredictionsystem/fqf.html')
 
def fuelQuoteHistory(request):
	return render(request, 'fuelpredictionsystem/fqh.html')
	
# def clientRegistration(request):
#     return render(request, 'fuelpredictionsystem/clientRegistration.html')
# def clientRegistration(request):
# 	if request.method == "POST":
# 		form = RegisterForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect("/home")
# 	else:
# 		form = RegisterForm()
# 		return render(request, "fuelpredictionsystem/clientRegistration.html", {"form":form})

def register(response):
	if response.method == 'POST':
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/home")
	else:
		form = RegisterForm()
		args = {"form":form}
	return render(response, "fuelpredictionsystem/clientRegistration.html", args)


# def profile(request):
# 	args = {'user': request.user}
# 	return render(request, 'fuelpredictionsystem/clientProfile.html', {"form":form})


def loginHome(request):
	return render(request, 'fuelpredictionsystem/loginHome.html')

def profile(request):
	args = {'user': request.user}
	return render(request, 'fuelpredictionsystem/clientProfile.html', args)

def editProfile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/clientProfile')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form':form}
		return render(request, 'fuelpredictionsystem/editProfile.html', args)


@login_required
def go_home_page(request):
	product = get_object_or_404(UserProfile)
	return render(request, 'fuelpredictionsystem/loginHome.html', {'product' : product})