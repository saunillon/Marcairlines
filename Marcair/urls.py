from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.index, name='index'),
]

"""Création des liens urls vers les différentes pages du site"""
urlpatterns = [
    # welcome page
    path('', views.index, name='homepage'),
    # Account, Login management 
    path('my-account/', views.client_access, name='client_account'),
    path('account-creation/', forms.IdentityForm, name='creation'),
    path('account-created/', views.get_identity, name='Account-created'),  
    # Webpages on flights infos
    path('flights/', views.FlightView.as_view(), name='flights'),
    path('flights/<int:pk>/', views.FlightDetailView.as_view(), name='flight-details'),
    # Webpages on departures infos
    path('departures/', views.DepartureView.as_view(), name='departures'),
    path('departures/<int:pk>/', views.DepartureDetailView.as_view(), name='departure-details'),
    # Webpages on departures airports
    path('airports/', views.AirportView.as_view(), name='airports'),
    path('airports/<int:pk>/', views.AirportDetailView.as_view(), name='airport-details'),
    # Webpages on airplanes infos
    path('airplanes/', views.AirplaneView.as_view(), name='airplanes'),
    path('airplanes/<int:pk>/', views.AirplaneDetailView.as_view(), name='airplane-details'),
    # Webpages on tickets infos
    path('ticket-list/', views.TicketView.as_view(), name='ticket_buy'),
    path('buy-tickets/', views.get_flight, name='buy-tickets'),
    # Webpages on company infos
    path('about-us/', views.about_us, name='infos'),
]