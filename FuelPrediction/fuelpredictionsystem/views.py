#from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, EditProfileForm, UserProfileFrom,FuelQuoteForm
# from .forms import RegisterForm, EditProfileForm, FuelQuoteForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile
from django.http import HttpResponseRedirect



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

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		profile_form = UserProfileFrom(request.POST)

		if form.is_valid() and profile_form.is_valid():
			user = form.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			
			return redirect("/home")
	else:
		form = RegisterForm()
		profile_form= UserProfileFrom()
	args = {"form":form, "profile_form":profile_form}
	return render(request, "fuelpredictionsystem/clientRegistration.html", args)


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
		p_form = EditProfileForm(request.POST, instance=request.user.userprofile)
		if form.is_valid() and p_form.is_valid():
			form.save()
			p_form.save()
			return redirect('/clientProfile')

	else:
		form = EditProfileForm(instance=request.user)
		p_form = EditProfileForm(request.POST, instance=request.user.userprofile)
		args = {'form':form, 'p_form':p_form}
		return render(request, 'fuelpredictionsystem/editProfile.html', args)


@login_required
def go_home_page(request):
	product = get_object_or_404(UserProfile)
	return render(request, 'fuelpredictionsystem/loginHome.html', {'product' : product})




def fuelQuoteForm(request):
	if request.method == 'POST':
		form = FuelQuoteForm(request.POST)
		if form.is_valid():
			# form.save()
			return render(request, 'fuelpredictionsystem/fqf.html', {"form":form})
		# return redirect("/fuelQuoteForm")
		#return HttpResponseRedirect(self.request.path_info)
	else:
		form = FuelQuoteForm()
	return render(request, 'fuelpredictionsystem/fqf.html', {"form":form})


# def fuelQuoteForm(request):
# 	if request.method == 'POST':
# 		form = FuelQuoteForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		# return redirect("/fuelQuoteForm")
# 		#return HttpResponseRedirect(self.request.path_info)
# 	else:
# 		form = FuelQuoteForm()
# 	return render(request, 'fuelpredictionsystem/fqf.html', {"form":form})

# def success(request):
# 	return render(request, 'fuelpredictionsystem/success.html')