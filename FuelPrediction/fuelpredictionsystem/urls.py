from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views
#from django.contrib.auth.views import login
from fuelpredictionsystem import views as v

urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    #path('home/', views.home, name='companySite-home'),
    path('clientProfile/', views.clientProfile, name='fuelpredictionsystem-clientProfile'),
    path('fqf/', views.fuelQuoteForm, name='fuelpredictionsystem-fqf'),
    path('fqh/', views.fuelQuoteHistory, name='fuelpredictionsystem-fqh'),
    #path('clientRegistration/', views.clientRegistration, name='clientRegistration'),
    path('clientRegistration/', views.register, name='clientRegistration'),
    path('success/', views.success)

]