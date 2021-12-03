import datetime
from django.views import generic
from django.shortcuts import get_object_or_404 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import reverse

from .forms import Buy_a_ticket_Form, IdentityForm

# Create your views here.
from Marcair.models import Airport, Flight, Departure, Ticket, Connection, Transaction, Pilot, Employee, CrewMember, Airplane, Client

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_flights = Flight.objects.all().count()
    num_departures = Departure.objects.all().count()
    num_airports = Airport.objects.all().count()
    num_flights2 = Flight.objects.raw('SELECT COUNT(*) FROM Flight;')
    num_departures2 = Departure.objects.raw('SELECT COUNT(*) FROM Departure;')
    num_airports2 = Airport.objects.raw('SELECT COUNT(*) FROM Airport;')


    # Available books (status = 'a')
    num_seat_available = Departure.objects.filter(number_of_empty_seat__exact='0').count()

    # The 'all()' is implied by default.
    num_pilots = Pilot.objects.count()

    context = {
        'num_flights': num_flights,
        'num_departures': num_departures,
        'num_airports': num_airports,
        'num_flights2': num_flights2,
        'num_departures2': num_departures2,
        'num_airports2': num_airports2,
        'num_seat_available': num_seat_available,
        'num_pilots': num_pilots,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def about_us(request):
    """View function for information of site."""
    context={ }
    # Render the HTML template about_us.html with the data in the context variable
    return render(request, 'about_us.html', context=context)


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
    context= {
        'listofflights':Flight.objects.raw('SELECT * FROM Flight')
    }
    # Render the HTML template about_us.html with the data in the context variable
    return render(request, 'Marcair/buying.html', context=context)

def get_identity(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IdentityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("{% url 'login'%}")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IdentityForm(request.GET)

    return render(request, 'Marcair/account_created.html', {'form': form})

def book_a_flight(request, pk):
    booking=get_object_or_404(Flight, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Buy_a_ticket_Form(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            booking.due_back = form.cleaned_data['renewal_date']
            booking.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('/') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = Buy_a_ticket_Form(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'Marcair/buying.html', {'form': form, 'booking':booking})
