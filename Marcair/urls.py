from django.urls import path, include
import django.contrib.auth.urls
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from . import forms
"""MarcAirlines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""Creation of url patterns for the different pages on the website"""
urlpatterns = [
    # welcome page
    path('', views.index, name='homepage'),

    path('my-account/', views.client_access, name='client_account'),
    #path('account_creation/', views.SignupView, name="account_creation"),

    # Webpages on infos
    path('flights/', views.FlightView.as_view(), name='flights'),
    path('flights/<int:pk>/', views.FlightDetailView.as_view(), name='flight-details'),
    path('departures/', views.DepartureView.as_view(), name='departures'),
    path('departures/<int:pk>/', views.DepartureDetailView.as_view(), name='departure-details'),
    path('airports/', views.AirportView.as_view(), name='airports'),
    path('airports/<int:pk>/', views.AirportDetailView.as_view(), name='airport-details'),
    path('airplanes/', views.AirplaneView.as_view(), name='airplanes'),
    path('airplanes/<int:pk>/', views.AirplaneDetailView.as_view(), name='airplane-details'),
    # Webpages on purchasing
    path('buy-tickets/', views.get_flight, name='buy-tickets'),
    # Webpages on company infos
    path('about-us/', views.about_us, name='infos'),
    path('register/', views.register, name='register'),
 
]