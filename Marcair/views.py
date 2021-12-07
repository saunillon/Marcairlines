
# import of the necessary extensions
import datetime
import io
import os
import random
from abc import ABC
from django.views import generic 
from django.shortcuts import render, reverse, redirect
from django.utils.http import urlencode
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404, FileResponse
from django.core.mail import send_mail
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from django import forms
from django.templatetags.static import static
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.db.models import Lookup
from django.contrib.auth.forms import UserCreationForm

# import the forms and the models created
from .forms import  FlightForm, ResearchForm
from Marcair.models import Airport, Flight, Departure, Ticket, Connection, Transaction, Pilot, Employee, CrewMember, Airplane, Client 
# CustomUser
# SignupForm,

# creation of the views

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_flights = Flight.objects.all().count()
    num_departures = Departure.objects.all().count()
    num_airports = Airport.objects.all().count()
    # Available books (status = 'a')
    num_seat_available = Departure.objects.filter(number_of_empty_seat__exact='0').count()
    # The 'all()' is implied by default.
    num_pilots = Pilot.objects.count()
    context = {"date": datetime.date.today(),
        'num_flights': num_flights,
        'num_departures': num_departures,
        'num_airports': num_airports,
        'num_seat_available': num_seat_available,
        'num_pilots': num_pilots,}
    try:
        context["user_name"] = request.user.first_name
    except AttributeError:
        context["user_nom"] = ""
    return render(request, "index.html", context=context)

def about_us(request):
    """View function for information of site."""
    context={ }
    # Render the HTML template about_us.html with the data in the context variable
    return render(request, 'about_us.html', context=context)

def register(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def client_access(request):
    """View function for information of site."""
    context = { }
    # Render the HTML template about_us.html with the data in the context variable
    return render(request, 'client_access.html', context=context)

class FlightView(generic.ListView):
    model = Flight

class DepartureView(generic.ListView):
    model = Departure

class ClientView(LoginRequiredMixin, generic.ListView):
    model = Client

class TicketView(LoginRequiredMixin, generic.ListView):
    model = Ticket

class AirportView(generic.ListView):
    model = Airport

class AirplaneView(generic.ListView):
    model = Airplane

class FlightDetailView(generic.DetailView):
    model = Flight

class DepartureDetailView(generic.DetailView):
    model = Departure

class AirportDetailView(generic.DetailView):
    model = Airport

class AirplaneDetailView(generic.DetailView):
    model = Airplane

def get_flight(request):
    """View function for information of site."""
    if request.method=="POST":
        form = ResearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Marcairbuying.html')
    else:
        form = ResearchForm()
        
    return render(request,'Marcair/buying.html',{'form':form})
    context= {
        
    }
    # Render the HTML template about_us.html with the data in the context variable
    return render(request, 'Marcair/buying.html', context=context)


class TicketDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Ticket
    template_name = "detail-ticket.html"
    # context_object_name = ""
    def test_func(self):
        ticket = Ticket.objects.get(pk=self.kwargs["pk"])
        return self.request.user.id == Ticket.client_id

class TicketReservations(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = "ticket_list.html"
    # paginate_by = 2
    permission_denied_message = "Please connect to see your tickets"
    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user).order_by("date_time_of_issue")

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        queries = self.get_queryset()
        # context["old_reservations"] = queries.exclude(trajet__date_depart__gt =datetime.date.today())
        # context["new_reservations"] = queries.filter(trajet__date_depart__gt =datetime.date.today())
        return context

class Buy_Ticket(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = "buying.html"
    personne = forms.SelectMultiple()
    fields = (
        'flight',
        'place',
    )
    widgets = {
        'trajet': forms.Textarea(attrs={'readonly': 'readonly'})
    }
    permission_denied_message = "Please connect to book a flight"
