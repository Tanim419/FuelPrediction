#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth.models import User


def index(request):
	#return HttpResponse("Tech with tim!")
	return render(request, 'fuelpredictionsystem/home.html')


# def home(request):
#     return HttpResponse("Tech with tim!")

def home(request):
	 return render(request, 'fuelpredictionsystem/home.html')
	
# def clientProfile(request):
# 	return render(request, 'fuelpredictionsystem/clientProfile.html')

# def fuelQuoteForm(request):
# 	return render(request, 'fuelpredictionsystem/fqf.html')
 
# def fuelQuoteHistory(request):
# 	return render(request, 'fuelpredictionsystem/fqh.html')
	
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
	return render(response, "fuelpredictionsystem/clientRegistration.html", {"form":form})


def profile(request):
	args = {'user': request.user}
	return render(request, 'fuelpredictionsystem/clientProfile.html', {"form":form})